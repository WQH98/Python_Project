import scrapy
from scrapy import Request
import os
import json


class ExamSpider(scrapy.Spider):
    name = "exam"
    allowed_domains = ["wangxiao.cn"]
    start_urls = ["https://ks.wangxiao.cn/"]

    def parse(self, resp, **kwargs):
        li_list = resp.xpath('//ul[@class="first-title"]/li')
        for li in li_list:
            first_title = li.xpath('./p/span/text()').extract_first()
            a_list = li.xpath('./div/a')
            for a in a_list:
                href = a.xpath('./@href').extract_first()
                second_title = a.xpath('./text()').extract_first()
                # 从模拟考试 到考点练习
                href = href.replace('TestPaper', 'exampoint')
                href = resp.urljoin(href)
                # print(first_title, second_title, href)
                # 发送请求 获取到考点练习的内容
                # yield Request(
                #     url=href,
                #     callback=self.parse_second,
                # )
                # 为了测试 只测试一个考点的
                yield Request(
                    url='https://ks.wangxiao.cn/exampoint/list?sign=jz1',
                    callback=self.parse_second,
                    meta={
                        'first_title': first_title,
                        'second_title': second_title,
                    },
                )
                return

    def parse_second(self, resp, **kwargs):
        # 拿到科目 这里对应着第三层文件夹
        # 在这里 可能需要之前获取的第一层类目和第二层类目的名字
        first_title = resp.meta['first_title']
        second_title = resp.meta['second_title']
        a_list = resp.xpath('//div[@class="filter-content"]/div[2]/a')
        for a in a_list:
            third_title = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            # print(third_title, href)
            href = resp.urljoin(href)
            yield Request(
                url=href,
                callback=self.parse_third,
                meta={
                    'first_title': first_title,
                    'second_title': second_title,
                    'third_title': third_title,
                },
            )
            # 测试用
            return

    def parse_third(self, resp, **kwargs):
        first_title = resp.meta['first_title']
        second_title = resp.meta['second_title']
        third_title = resp.meta['third_title']
        # print(first_title, second_title, third_title)
        chapters = resp.xpath('//ul[@class="chapter-item"]')
        for chapter in chapters:
            sections = chapter.xpath('.//ul[@class="section-point-item"]')
            if sections:
                # 最底层是section-item
                for section in sections:
                    # 此时section就是最底层
                    # 1、处理上层嵌套逻辑
                    # ancestor 找到当前节点的祖先节点
                    titles = []
                    items = section.xpath('./ancestor::ul[@class="section-item" or @class="chapter-item"]')
                    for item in items:
                        title = "".join(item.xpath("./li[1]//text()").extract()).strip()
                        titles.append(title)
                    # print(titles)
                    # 拼接路径
                    # 在实参位置 *表示把一个可迭代内容打散成位置参数
                    file_path = os.path.join(first_title, second_title, third_title, *titles).replace(' ','')
                    # 2、处理自己
                    file_name = "".join(section.xpath("./li[1]//text()").extract()).strip().replace(' ', '')
                    list_question_url = 'https://ks.wangxiao.cn/practice/listQuestions'
                    sign = section.xpath('./li[3]/span/@data_sign').extract_first()
                    subsign = section.xpath('./li[3]/span/@data_subsign').extract_first()
                    top = section.xpath('./li[2]//text()').extract_first().split('/')[-1]
                    data = {
                        'examPointType': "",
                        'practiceType': "2",
                        'questionType': "",
                        'sign': sign,
                        'subsign': subsign,
                        'top': top
                    }
                    print(file_path, file_name)
                    yield Request(
                        url=list_question_url,
                        method='POST',
                        body=json.dumps(data),
                        headers={
                            'Content-Type': 'application/json;charset=UTF-8'
                        },
                        callback=self.parse_fouth,
                        meta={
                            'file_path': file_path,
                            'file_name': file_name
                        }
                    )
                    return
            else:
                # 当前已经是最底层了section-point-item
                file_path = os.path.join(first_title, second_title, third_title).replace(' ', '')
                file_name = "".join(chapter.xpath("./li[1]//text()").extract()).strip()
                list_question_url = 'https://ks.wangxiao.cn/practice/listQuestions'
                sign = chapter.xpath('./li[3]/span/@data_sign').extract_first()
                subsign = chapter.xpath('./li[3]/span/@data_subsign').extract_first()
                top = chapter.xpath('./li[2]//text()').extract_first().split('/')[-1]
                data = {
                    'examPointType': "",
                    'practiceType': "2",
                    'questionType': "",
                    'sign': sign,
                    'subsign': subsign,
                    'top': top
                }
                print(file_path, file_name)
                yield Request(
                    url=list_question_url,
                    method='POST',
                    body=json.dumps(data),
                    headers={
                        'Content-Type': 'application/json;charset=UTF-8'
                    },
                    callback=self.parse_fouth,
                    meta={
                        'file_path': file_path,
                        'file_name': file_name
                    }
                )
                return

    def parse_fouth(self, resp, **kwargs):
        file_path = resp.meta['file_path']
        file_name = resp.meta['file_name']
        # print(resp.json())
        items = resp.json()["Data"]
        # 循环出题型对应的题目
        for item in items:
            questions = item.get('questions')
            # 是个列表 有题
            if questions:
                # 这次循环出来的是个列表
                for question in questions:
                    # 题目本身
                    content, analysis = self.parse_question(question)
                    question_info = content + '\n' + analysis
                    # 题目答案
                    yield {
                        'file_path': file_path,
                        'file_name': file_name,
                        'question_info': question_info,
                    }
            # 材料题 题的逻辑与上面不一样
            else:
                materials = item.get('materials')
                for mater in materials:
                    material = mater.get('material')
                    material_content = material.get('content')
                    questions = mater.get('questions')
                    question_list = []
                    for question in questions:
                        content, analysis = self.parse_question(question)
                        one_question = content + '\n' + analysis
                        question_list.append(one_question)
                    question_info = '\n'.join(question_list)
                    question_info = material_content + '\n' + question_info
                    yield {
                        'file_path': file_path,
                        'file_name': file_name,
                        'question_info': question_info,
                    }

    def parse_question(self, question):
        content = question.get('content')
        options = question.get('options')
        option_list = []
        right_list = []
        for option in options:
            opt_name = option.get('name')
            opt_content = option.get('content')
            option_list.append(opt_name + ',' + opt_content)
            is_right = option.get('is_right')
            if is_right:
                right_list.append(opt_name)
                # pass   # 正确答案
        content += '\n'.join(option_list)
        analysis = '正确答案是' + ','.join(right_list) + '\n' + question.get('textAnalysis')
        return content, analysis
