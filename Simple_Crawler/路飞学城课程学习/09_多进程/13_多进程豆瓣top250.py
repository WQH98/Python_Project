import random
import time
import requests
from multiprocessing import Pool
from lxml import etree


def build_url():
    url_list = []
    for i in range(0, 250, 25):
        url_list.append(f"https://movie.douban.com/top250?start={i}&filter=")
    return url_list


def get_page_title(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.content.decode())
    titles = tree.xpath('//div[@class="hd"]/a/span[1]/text()')
    print(len(titles))
    time.sleep(random.randint(4, 5))


if __name__ == '__main__':
    urls = build_url()
    pool = Pool(3)
    for url in urls:
        pool.apply_async(get_page_title, args=(url, ))
    pool.close()
    pool.join()

