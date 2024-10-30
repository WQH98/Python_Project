import requests
from lxml import etree

url = 'https://app.mi.com/catTopList/0?'

params = {
    'page': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}

res = requests.get(url)
content = res.content.decode('utf-8')

tree = etree.HTML(content)
# 抓取应用名称和超链接
app_lists = tree.xpath('//ul[@class="applist"]//li')
for app in app_lists:
    print(app.xpath('./h5/a/text()'), app.xpath('./h5/a/@href'))

