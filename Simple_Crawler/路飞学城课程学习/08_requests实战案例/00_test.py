import requests
from lxml import etree

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}

response = requests.get(url, headers=headers).content.decode()
tree = etree.HTML(response)
path1 = tree.xpath('//div[@class="card bookmark-list"]/h1/text()')[0]
print(path1)
