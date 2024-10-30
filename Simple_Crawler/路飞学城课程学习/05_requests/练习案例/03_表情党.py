import requests
from lxml import etree

url = 'https://qq.yh31.com/xq/wq/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}

res = requests.get(url, headers=headers)
content = res.content.decode('utf-8')
tree = etree.HTML(content)
lis = tree.xpath('//div[@class="sr"]//li')
for li in lis:
    img_url = li.xpath('./dt/a/img/@data-src')
    img_type = img_url[0][-3:]
    img_name = li.xpath('./dd/a/text()')
    img = requests.get(img_url[0], headers=headers)
    with open(f'./表情党图片/{img_name[0]}.{img_type}', 'wb') as f:
        f.write(img.content)
