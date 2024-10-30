# 抓取热辣滚烫 使用进程的方式
import os
import requests
from multiprocessing import Pool
import time
import re


def get_html_cookies(session, url, headers):
    for i in range(10):
        try:
            session.get(url, headers=headers)
            print("获取Cookie成功")
            return session
        except Exception as e:
            print(e)
            print("获取Cookie失败 5秒后重试")
            time.sleep(5)
    return session


def get_first_m3u8_source(session, url, headers):
    #                                                        2000k/hls/mixed.m3u8
    # https://svipsvip.ffzyread1.com/20240418/26209_829902db/2000k/hls/mixed.m3u8
    res = session.get(url, headers=headers)
    m3u8_url = re.findall(r'#EXT-X-STREAM-INF:.*\n(.*)', res.text)[-1]
    return 'https://svipsvip.ffzyread1.com/20240418/26209_829902db/' + m3u8_url


def get_second_m3u8_source(session, url, headers, path):
    res = session.get(url, headers=headers)
    with open(f'{path}/index.m3u8', 'w', encoding='utf-8') as f:
        f.write(res.text)


def get_movie_urls(url, path):
    movie_urls = []
    with open(f'{path}/index.m3u8', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('#'):
            continue
        movie_urls.append(f'{url}' + line.strip())
    return movie_urls


def download_one_movie(session, url, headers, path, name):
    for i in range(10):
        try:
            res = session.get(url, headers=headers)
            with open(f'{path}/{name}.ts', 'wb') as f:
                f.write(res.content)
            print(f"下载{url}成功 延时5秒")
            time.sleep(5)
            return
        except Exception as e:
            print(e)
            print(f"下载{url}失败 5秒后重试")
            time.sleep(5)
    return


if __name__ == '__main__':
    session = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    cookies_url = 'https://www.uuoozz.com/movie/'
    session = get_html_cookies(session, cookies_url, headers)
    path = "./下载"
    if not os.path.exists(path):
        print('未找到下载文件夹 现在创建')
        os.makedirs(path)
    first_m3u8_url = 'https://svipsvip.ffzyread1.com/20240418/26209_829902db/index.m3u8'
    second_m3u8_url = get_first_m3u8_source(session, first_m3u8_url, headers)
    print("成功得到第二个m3u8的网址是", second_m3u8_url)
    get_second_m3u8_source(session, second_m3u8_url, headers, path)
    # movie_url = 'https://svipsvip.ffzyread1.com/20240418/26209_829902db/2000k/hls/'
    # movie_list = get_movie_urls(movie_url, path)
    # names = []
    # for i in range(len(movie_list)):
    #     names.append(i)
    # pool = Pool(5)
    # for i in range(len(movie_list)):
    #     pool.apply_async(download_one_movie, args=(session, movie_list[i], headers, path, names[i]))
    # # pool.map(download_one_movie, session, movie_list, headers, path, names)
    # pool.close()
    # pool.join()

