import time

import requests
from lxml import etree
import pandas as pd

def get_url():
    url_list = []
    for i in range(0, 100, 20):
        url_list.append(f'https://movie.douban.com/review/best/?start={i}')
    return url_list


def get_context(url):
    ret_datas = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    }
    res = requests.get(url, headers=headers)
    content = res.content.decode()
    tree = etree.HTML(content)
    divs = tree.xpath('//div[@class="review-list chart "]/div')
    for div in divs:
        img = div.xpath('.//img/@src')[0]
        title = div.xpath('.//div[@class="main-bd"]/h2/a/text()')[0]
        name = div.xpath('.//img/@alt')[0]
        review_url = div.xpath('.//div[@class="main-bd"]/h2/a/@href')[0]
        review_content = requests.get(review_url, headers=headers).content.decode()
        review_tree = etree.HTML(review_content)
        review = review_tree.xpath('//div[@class="review-content clearfix"]/p/text()')
        review = ' '.join(review)
        subject_url = div.xpath('.//a[@class="subject-img"]/@href')[0]
        subject_content = requests.get(subject_url, headers=headers).content.decode()
        subject_tree = etree.HTML(subject_content)
        subject = subject_tree.xpath('//span[@property="v:summary"]//text()')
        subject = ' '.join(subject).strip()
        ret_datas.append([name, title, img, review, subject])
    return ret_datas


if __name__ == "__main__":
    datas = []
    urls = get_url()
    for url in urls:
        datas += get_context(url)
        time.sleep(1)
    df = pd.DataFrame(datas, columns=['电影名字', '评论标题', '图片地址', '完整评论', '简介'])
    df.to_excel('./豆瓣影评附件/豆瓣影评.xlsx', index=False)

