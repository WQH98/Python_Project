import requests
from lxml import etree

url = 'https://www.qqtn.com/wm/meinvtp_1.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}

res = requests.get(url, headers=headers)
content = res.content.decode('gbk')
tree = etree.HTML(content)
lis = tree.xpath('//ul[@class="g-gxlist-imgbox"]/li')
for li in lis:
    img_urls = li.xpath('./a/img/@src')
    img_name = li.xpath('./a/strong/text()')
    img = requests.get(img_urls[0], headers=headers)
    with open(f'./腾牛网图片/{img_name}.jpg', 'wb') as f:
        f.write(img.content)





