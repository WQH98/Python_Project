import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
url = 'http://www.cs.ecitic.com/newsite/cpzx/jrcpxxgs/zgcp/index.html'
res = requests.get(url, headers=headers)
res.encoding = res.apparent_encoding
data = res.text
# print(data)
tree = etree.HTML(data)
# text = tree.xpath('//ul[@class="list-con"]/li/span/text()')
li_list = tree.xpath('//ul[@class="list-con"]/li')
# print(text)
for li in li_list:
    print(li.xpath('./span/text()'))