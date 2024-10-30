"""
    存在问题 有的ts文件下载下来以后只有1K
    暂时不知道怎么修改
"""

import os
import time
import requests
import re
from concurrent.futures import ThreadPoolExecutor, wait


class class_main():
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
        }
        self.session = requests.session()
        self.movie_m3u8_url = 'https://v7.tlkqc.com/wjv7/202404/17/S2EBcuGKVs79/video/index.m3u8'

    def get_cookies(self):
        url = 'https://www.dsxysw.com/'
        self.session.get(url, headers=self.headers)

    def get_first_m3u8(self):
        res = self.session.get(self.movie_m3u8_url, headers=self.headers)
        res.encoding='utf-8'
        with open('first_index.txt', 'w', encoding='utf-8') as f:
            f.write(res.text)

    def get_first_m3u8_url(self):
        with open('first_index.txt', 'r', encoding='utf-8') as f:
            data = f.read()
        res = re.search(("(.+?index.m3u8)"), data).group(1)
        return "https://v7.tlkqc.com/wjv7/202404/17/S2EBcuGKVs79/video/" + res

    def get_second_m3u8(self, url):
        res = self.session.get(url, headers=self.headers)
        res.encoding = 'utf-8'
        with open('second_index.txt', 'w', encoding='utf-8') as f:
            f.write(res.text)

    def get_second_m3u8_url(self):
        data = []
        with open('second_index.txt', 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                data.append(line)
        with open('url.txt', 'w', encoding='utf-8') as f:
            f.writelines(data)

    def download_m3u8(self, url, i, path):
        time.sleep(2)
        print(i, "开始下载")
        res = self.session.get(url, headers=self.headers)
        with open(f'{path}/{i}.ts', 'wb') as f:
            f.write(res.content)
        print(i, "完成下载")
        time.sleep(2)


if __name__ == '__main__':
    class1 = class_main()
    # class1.get_cookies()
    # class1.get_first_m3u8()
    # first_m3u8_url = class1.get_first_m3u8_url()
    # class1.get_second_m3u8(first_m3u8_url)
    # class1.get_second_m3u8_url()
    i = 0
    path = "./大师兄视频下载"
    if not os.path.exists(path):
        os.makedirs(path)
    pool = ThreadPoolExecutor(50)
    tasks = []
    with open('url.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        tasks.append(pool.submit(class1.download_m3u8, line, i, path))
        i += 1
    wait(tasks)

