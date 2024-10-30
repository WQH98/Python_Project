# 抓取热辣滚烫 使用线程的方式
import os
import time
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor, wait


def get_cookies(url, session, headers):
    print("开始获取cookies")
    for i in range(10):
        try:
            session.get(url, headers=headers)
            print("获取cookies成功")
            return session
        except Exception as e:
            print(e)
            print("获取cookies失败 5秒后重试")
            time.sleep(5)
    exit("获取cookies失败 请检查")


def get_m3u8_url(url, session, headers):
    print("开始获取m3u8的网址")
    res = session.get(url, headers=headers)
    tree = etree.HTML(res.text)
    m3u8_url = tree.xpath('//div[@class="video"]/iframe/@src')[0].split('=')[-1]
    print("获取成功 ", m3u8_url)
    return m3u8_url


def save_m3u8_page(url, session, headers, path, name):
    print("将m3u8文件保存在本地")
    res = session.get(url, headers=headers)
    with open(f'{path}/{name}', 'w') as f:
        f.write(res.text)
    print("保存成功")


def get_movie_url_list(path, name, url):
    print("开始读取m3u8文件 并构建ts文件列表")
    movie_url_list = []
    with open(f'{path}/{name}', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('#'):
            continue
        movie_url_list.append(url + line.strip())
    print("构建成功")
    return movie_url_list


def download_one_ts(url, session, header, path, name):
    print("开始下载 ", url)
    for i in range(10):
        try:
            res = session.get(url, headers=header)
            with open(f'{path}/{name}.ts', 'wb') as f:
                f.write(res.content)
            print("下载成功 ", url, "等待3秒")
            time.sleep(3)
            return
        except Exception as e:
            print(e)
            print("下载 ", url, " 失败 五秒后重试")
            time.sleep(5)
    print("下载失败 ", url, "请检查")
    exit()


if __name__ == '__main__':
    session = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    path = './下载'
    m3u8_name = 'index.m3u8'
    if not os.path.exists(path):
        print("未找到下载文件夹 现在创建")
        os.makedirs(path)
    cookies_url = 'https://www.uuoozz.com/movie/'
    session = get_cookies(cookies_url, session, headers)
    movie_url = 'https://www.uuoozz.com/play/1778_1_1.html'
    m3u8_url = get_m3u8_url(movie_url, session, headers)
    save_m3u8_page(m3u8_url, session, headers, path, m3u8_name)
    movie_url = 'https://s5.bfengbf.com/video/shaqiu2/HD/'
    movie_url_list = get_movie_url_list(path, m3u8_name, movie_url)
    pool = ThreadPoolExecutor(20)
    tasks = []
    i = 0
    for url in movie_url_list:
        task = pool.submit(download_one_ts, url, session, headers, path, i)
        tasks.append(task)
        i += 1
    wait(tasks)


