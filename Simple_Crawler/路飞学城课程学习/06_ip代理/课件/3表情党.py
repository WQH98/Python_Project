import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
url = 'https://qq.yh31.com/xq/wq/'
res = requests.get(url, headers=headers)
res.encoding = res.apparent_encoding
data = res.text
tree = etree.HTML(data)
print(data)
url_list = tree.xpath('//div[@class="sr"]//@data-src')
print(url_list)