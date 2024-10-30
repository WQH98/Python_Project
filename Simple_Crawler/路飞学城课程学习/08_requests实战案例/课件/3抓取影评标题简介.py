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
    # 简介
    short_content = d.xpath('./div//div[@class="short-content"]/text()')
    print(short_content)
