import requests
from lxml import etree
'''
练习xpath的复杂写法，多层嵌套 
以及element会自动补充标签tbody的坑
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
url = 'http://bbs.chinaunix.net/'
req = requests.get(url, headers=headers)
print(req.text)
tree = etree.HTML(req.text)
table = tree.xpath('//div[@style="clear:both; margin-bottom:10px"]/table/tbody[2]/tr/td/table/tr/td[2]/a/text()')
print(table)