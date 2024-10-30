import random
import time

import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
'''
https://movie.douban.com/top250?start=0&filter=
https://movie.douban.com/top250?start=25&filter=
https://movie.douban.com/top250?start=50&filter=
'''
# 获取10页数据
for i in range(1, 11):
    start = (i - 1) * 25
    url = f'https://movie.douban.com/top250?start={start}&filter='
    res = requests.get(url, headers=headers)
    # print(res.status_code)
    text = res.content.decode()
    tree = etree.HTML(text)
    # div = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div')
    div = tree.xpath('//*[@id="content"]/div/div[1]/ol/li/div')
    for d in div:
        # 获取评分
        rating_num = d.xpath('./div[2]/div[2]/div/span[2]/text()')
        # 评价人数
        comment = d.xpath('./div[2]/div[2]/div/span[4]/text()')
        print(comment)
    time.sleep(random.randint(1,3))