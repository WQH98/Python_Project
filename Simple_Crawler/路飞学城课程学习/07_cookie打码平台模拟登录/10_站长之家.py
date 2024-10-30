import os.path
import random
import time

from requests.adapters import HTTPAdapter
import requests
from lxml import etree
from urllib3 import Retry


def get_url(page_totla):
    urls = ['https://sc.chinaz.com/tupian/renwutupian_4.html']
    for i in range(2, page_totla + 1):
        urls.append(f'https://sc.chinaz.com/tupian/renwutupian_{i}.html')
    print(f"总共的页数 {len(urls)}")
    return urls


def get_page_img_url(urls):
    img_urls = []
    for url in urls:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        }
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=Retry(total=5)))  # 设置 post()方法进行重访问
        s.mount('https://', HTTPAdapter(max_retries=Retry(total=5))) # 设置 post()方法进行重访问
        res = s.get(url, headers=headers)
        tree = etree.HTML(res.content.decode())
        divs = tree.xpath('//div[@class="tupian-list com-img-txt-list"]/div')
        for div in divs:
            img_url = "https://sc.chinaz.com" + div.xpath('./div/a[@class="name"]/@href')[0]
            img_urls.append(img_url)
            print(f"get page url {img_url}")
    return img_urls


def download_img(urls):
    i = 0;
    path = "./10_站长之家图片下载"
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"未找到下载文件夹 现在新建 {path} 文件夹")
    print(f"共找到了{len(urls)}张图片")
    for url in urls:
        i += 1
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        }
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=Retry(total=5)))  # 设置 post()方法进行重访问
        s.mount('https://', HTTPAdapter(max_retries=Retry(total=5)))  # 设置 post()方法进行重访问
        res = s.get(url, headers=headers)
        try:
            tree = etree.HTML(res.content.decode('utf-8'))
        except:
            print("当前url有问题 没有文件 直接跳过")
            continue
        img_url = "http:" + tree.xpath('//div[@class="img-box"]/img/@src')[0]
        img_name = tree.xpath('//div[@class="img-box"]/img/@alt')[0]
        img_type = img_url.split('.')[-1]
        res = requests.get(img_url, headers=headers)
        with open(f'{path}/{img_name}.{img_type}', 'wb') as f:
            f.write(res.content)
            sleep_num = random.randint(1, 2)
            print(f"{i}/{len(urls)}  {img_name} 下载完成 延时{sleep_num}秒")
        time.sleep(sleep_num)


if __name__ == '__main__':
    page_totla = int(input("请输入总共想要下载的页数（每页大概40张照片）："))
    urls = get_url(page_totla)
    img_urls = get_page_img_url(urls)
    download_img(img_urls)
