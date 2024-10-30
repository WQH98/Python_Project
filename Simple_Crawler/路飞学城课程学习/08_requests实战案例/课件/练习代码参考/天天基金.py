import requests
from lxml import etree
'''
天天基金
'''

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

url = 'http://fundf10.eastmoney.com/jbgk_004400.html'
res = requests.get(url, headers=headers)
# print(res.content.decode('UTF-8'))
res.encoding = res.apparent_encoding
print(res.text)
tree = etree.HTML(res.text)
text = tree.xpath('//table[@class="info w790"]/tr//text()')
print(text)
