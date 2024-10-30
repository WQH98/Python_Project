"""
需求
抓取标题 作者 标签 内容
存进数据库
"""
import random
import time

import pymysql
import requests
from lxml import etree

url = 'https://www.xigushi.com/lzgs/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
}

db = pymysql.connect(host='localhost', user='root', password='admin', database='wuqi')
db.set_charset('utf8')
cursor = db.cursor()
res = requests.get(url, headers=headers)
print("爬取总页面成功")
res.encoding = 'utf-8'
tree = etree.HTML(res.text)
urls = tree.xpath('//div[@class="list"]/dl/dd/ul/li/a/@href')
page_urls = []
for url in urls:
    page_urls.append("https://www.xigushi.com/" + url)
print('获得了所有文章的网页 开始读文章')
for page_url in page_urls:
    res = requests.get(page_url, headers=headers)
    print(f'爬取{page_url}成功')
    res.encoding = 'utf-8'
    tree = etree.HTML(res.text)
    # 抓取标题
    title = tree.xpath('//div[@class="by"]/dl/dd/h1/text()')[0]
    # 抓取详情
    info1 = tree.xpath('//div[@class="by"]/dl/dd/div[@class="info"]//text()')[0].strip()
    info2 = tree.xpath('//div[@class="by"]/dl/dd/div[@class="info"]//text()')[1].strip()
    info = info1 + info2
    # 抓取文章内容
    ps = tree.xpath('//div[@class="by"]/dl/dd/p//text()')
    text = ""
    for p in ps:
        text += p.strip() + '\n'
    text = text.replace('"', '')
    sql = f'insert into user values("{title}", "{info}", "{text}")'
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        print(sql)
        db.rollback()
    time.sleep(random.random() + 0.5)

# 关闭数据库
db.close()
