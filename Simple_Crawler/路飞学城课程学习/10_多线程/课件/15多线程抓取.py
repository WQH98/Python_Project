import os.path
import random
import time
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor, wait

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

def get_img_src(page):
    '''
    抓取页面的图片的src
    :return:
    '''
    for i in range(1, page+1):
        url = f'https://www.pkdoutu.com/photo/list/?page={i}'
        print(f'抓取{url}页数据')
        res = requests.get(url, headers=headers)
        res.encoding = res.apparent_encoding
        tree = etree.HTML(res.text)
        # 抓取图片
        img_list = tree.xpath('//img[@referrerpolicy="no-referrer"]/@data-original')
        yield img_list

def download_img(url):
    '''
    下载图片
    :return:
    '''
    time.sleep(random.uniform(0, 1))
    img_res = requests.get(url, headers=headers)
    img_name = url.split('_')[-1]  # 通过图片url进行拆分，拿到图片名称和后缀
    path = 'img'
    # 判断路径是否存在，不存在则创建
    if not os.path.exists(path):
        os.mkdir(path)
    # 写入到文件中
    with open(os.path.join(path, img_name), 'wb') as f:
        f.write(img_res.content)


if __name__ == '__main__':
    # 线程池
    pool = ThreadPoolExecutor()
    """
    # 通过生成器get_img_src返回图片列表
    for url_list in get_img_src(5):
        # 循环加入线程
        pool.map(download_img, url_list)
    """
    task_list = []
    for url_list in get_img_src(5):
        task_list.extend(pool.submit(download_img, url) for url in url_list)
    wait(task_list)


