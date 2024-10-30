import os
import random
import time

import requests
from lxml import etree


def build_url():
    url = 'https://pic.netbian.com/index.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    response = requests.get(url, headers=headers)
    tree = etree.HTML(response.content.decode('GBK'))
    total_page = tree.xpath('//div[@class="page"]/a/text()')[-2]
    print(f"There are {total_page} pages in all")
    urls = []
    img_urls =[]
    urls.append(url)
    for i in range(2, 3):
        urls.append(f"https://pic.netbian.com/index_{i}.html")
    for url in urls:
        response = requests.get(url, headers=headers)
        tree = etree.HTML(response.content.decode('GBK'))
        hrefs = tree.xpath('//ul[@class="clearfix"]/li[not(@class)]/a/@href')
        for href in hrefs:
            img_urls.append(f"https://pic.netbian.com{href}")
    return img_urls


def download_img(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    response = requests.get(url, headers=headers)
    tree = etree.HTML(response.content.decode('GBK'))
    img_name = tree.xpath('//div[@class="photo-hd"]//text()')[0].replace('*', '_')
    img_url = 'https://pic.netbian.com/' + tree.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
    img_type = img_url.split('.')[-1]

    path = './彼岸图网下载图片'
    if not os.path.exists(path):
        os.mkdir(path)
    print(f'start {path}/{img_name}.{img_type}')
    response = requests.get(img_url, headers=headers).content
    with open(f'{path}/{img_name}.{img_type}', 'wb') as f:
        f.write(response)


if __name__ == "__main__":
    urls = build_url()
    print('get url success')
    for url in urls:
        download_img(url)
        time.sleep(random.randint(2, 3))
