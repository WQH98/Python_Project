import os.path
import random
import time
import requests
from lxml import etree
from multiprocessing import Pool


def build_url():
    url_list = []
    for i in range(39, 35, -1):
        url_list.append(f'https://qq.yh31.com/xq/wq/List_{i}.html')
    return url_list


def download_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    try:
        res = requests.get(url, headers=headers)
        return res
    except:
        print("下载图片数据失败 5秒后重试")
        time.sleep(5)
        download_data(url)


def download_img(url):
    response = download_data(url)
    tree = etree.HTML(response.content.decode())
    lis = tree.xpath('//div[@class="sr"]//li')
    path = "./14_多进程下载表情党图片"
    if not os.path.exists(path):
        print("未找到下载目录 现在新建目录")
        os.mkdir(path)
    for li in lis[0: 5]:
        img_url = li.xpath('./dt/a/img/@data-src')[0]
        img_name = li.xpath('./dt/a/img/@alt')[0]
        img_type = img_url.split('.')[-1]
        with open(f'{path}/{img_name}.{img_type}', 'wb') as f:
            f.write(download_data(img_url).content)
        print(f"下载 {img_name}.{img_type} 成功")
        time.sleep(random.randint(4, 5))


if __name__ == '__main__':
    urls = build_url()
    pool = Pool(2)
    pool.map(download_img, urls)
    pool.close()
    pool.join()
