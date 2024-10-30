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
# div = tree.xpath('//div[@class="review-list chart "]/div/div')
div = tree.xpath('//div[@class="main review-item"]')
# print(div)
for d in div:
    # 获取详情超链接
    href = d.xpath('./a/@href')
    # short_content = d.xpath('./div/div[1]/div/text()')
    # 简短简介
    short_content = d.xpath('./div//div[@class="short-content"]/text()')
    # 获取完整简介的idz值 用于拼接完整的简介的url
    r_id = d.xpath('./@id')[0]
    # 请求完整简介的url
    r_url = f'https://movie.douban.com/j/review/{r_id}/full'
    r_res = requests.get(r_url, headers=headers)
    print(r_res.json()['html'])
    time.sleep(random.randint(1, 3))

'''
# 分析完整简介的url
https://movie.douban.com/j/review/14584121/full
https://movie.douban.com/j/review/14576114/full
'''