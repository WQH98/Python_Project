import time
import requests
from lxml import etree
import pandas as pd


def build_url():
    url_list = []
    for i in range(0, 250, 25):
        url = f'https://movie.douban.com/top250?start={i}&filter='
        url_list.append(url)
    return url_list


def list_to_str(list):
    if not list:
        list = ""
    else:
        list = list[0]
    return list


def get_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    res = requests.get(url, headers=headers)
    content = res.content.decode()
    tree = etree.HTML(content)
    lis = tree.xpath('//ol[@class="grid_view"]/li')
    datas = []
    for li in lis:
        name = li.xpath('.//div[@class="hd"]//span[@class="title"][1]/text()')
        name = list_to_str(name)
        score = li.xpath('.//div[@class="star"]//span[@class="rating_num"]/text()')
        score = list_to_str(score)
        intro = li.xpath('.//span[@class="inq"]/text()')
        intro = list_to_str(intro)
        people = li.xpath('.//div[@class="star"]/span[4]/text()')
        people = list_to_str(people)
        datas.append([name, score, intro, people])
    return datas


if __name__ == "__main__":
    url_list = build_url()
    datas = []
    res = []
    for url in url_list:
        print(f'start {url}')
        datas.append(get_content(url))
        time.sleep(1)
    for data in datas:
        for d in data:
            res.append(d)
    df = pd.DataFrame(res, columns=['名字', '分数', '简介', '评分人数'])
    df.to_excel('./豆瓣top250附件/豆瓣.xlsx', index=False)

