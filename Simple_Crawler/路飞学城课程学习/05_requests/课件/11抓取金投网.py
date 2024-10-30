import requests
from lxml import etree

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
url = 'https://cang.cngold.org/c/2022-06-14/c8152503.html'

res = requests.get(url, headers=headers)
content = res.content.decode()
tree = etree.HTML(content)
text = tree.xpath('//table[@border="1"]/tbody/tr/td/text()')
# print(text)
# 练习
# 去除第一行的内容
