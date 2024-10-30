import requests
from lxml import etree

url = 'https://cang.cngold.org/c/2022-06-14/c8152503.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}

res = requests.get(url, headers=headers)

content = res.content.decode('utf-8')

tree = etree.HTML(content)

trs = tree.xpath('//table[@border="1"]/tbody//tr')[1:]
for tr in trs:
    print(tr.xpath('.//td/text()'))


