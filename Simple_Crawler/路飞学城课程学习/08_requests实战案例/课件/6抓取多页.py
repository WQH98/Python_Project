import random
import time
import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
url = 'https://movie.douban.com/review/best/'
res = requests.get(url, headers=headers)
text = res.content.decode()
tree = etree.HTML(text)
div = tree.xpath('//div[@class="main review-item"]')
for d in div:
    # 获取详情超链接
    href = d.xpath('./a/@href')[0]
    print(href)
'''
https://movie.douban.com/review/best/?start=0
https://movie.douban.com/review/best/?start=20
https://movie.douban.com/review/best/?start=40
'''
for i in range(0, 100, 20):
    print(f'https://movie.douban.com/review/best/?start={i}')