import requests
from lxml import etree

url = 'https://app.mi.com/catTopList/0?page=1'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=headers)
content = res.content.decode()
tree = etree.HTML(content)
# 抓取应用名称
# app_name = tree.xpath('//ul[@class="applist"]/li/h5/a/text()')
# 超链接
# a_list = tree.xpath('//ul[@class="applist"]/li/h5/a/@href')
# print(app_name)
# print(a_list)
# print(tree.xpath('//ul[@class="applist"]/li/h5/a/text() | //ul[@class="applist"]/li/h5/a/@href'))

a_list = tree.xpath('//ul[@class="applist"]/li/h5/a')
# print(a_list)
for a in a_list:
    print(a.xpath('./text()'))
    print(a.xpath('./@href'))