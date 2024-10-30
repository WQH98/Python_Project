# 使用协程抓取视频
import aiofiles
import aiohttp
import requests
import asyncio
from bs4 import BeautifulSoup
import time
import os
import re


def get_cookies(session, url, headers):
    print('开始获取cookies')
    session.get(url, headers=headers)
    print('获取cookies成功')
    return session


def get_m3u8_source(session, url, headers, path, m3u8_file_name):
    print('开始寻找第一个m3u8网址')
    res = session.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    first_m3u8_url = soup.find('div', class_="video").find('iframe')['src'].split('=')[-1]
    print('第一个m3u8网址为：', first_m3u8_url)
    print('开始寻找第二个m3u8网址')
    res = session.get(first_m3u8_url, headers=headers)
    second_m3u8_url = 'https://svipsvip.ffzyread1.com/20240321/25390_ea25721a/' + re.search('(.*m3u8)', res.text).group(0)
    print('得到第二个m3u8网址为：', second_m3u8_url)
    print('开始将第二个m3u8的内容保存在本地')
    res = session.get(second_m3u8_url, headers=headers)
    with open(f'{path}/{m3u8_file_name}', 'w') as f:
        f.write(res.text)
    print("保存成功")


def get_movies_url_list(path, m3u8_file_name):
    with open(f'{path}/{m3u8_file_name}', 'r') as f:
        lines = f.readlines()
    movies_url_list = []
    for line in lines:
        if line.startswith('#'):
            continue
        movies_url_list.append('https://svipsvip.ffzyread1.com/20240321/25390_ea25721a/2000k/hls/' + line.strip())
    return movies_url_list


async def download_one_ts(url, headers, path, name, signal, cookies):
    for i in range(10):
        try:
            async with signal:
                print(f'开始下载 {url}')
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, headers=headers, cookies=cookies) as response:
                        async with aiofiles.open(f'{path}/{name}.ts', 'wb') as f:
                            await f.write(await response.read())
                print(f"下载成功 {url} 延时1秒")
                await asyncio.sleep(1)
                return
        except Exception as e:
            print(e)
            print(f'下载 {url} 失败 5秒后重试')
            await asyncio.sleep(5)
    print(f'下载 {url} 失败')
    exit()


async def download_all_ts(movies_url_list, headers, path, cookies):
    tasks = []
    semaphore = asyncio.Semaphore(10)
    i = 0
    for url in movies_url_list:
        con = download_one_ts(url, headers, path, i, semaphore, cookies)
        task = asyncio.create_task(con)
        tasks.append(task)
        i += 1
    await asyncio.wait(tasks)


if __name__ == '__main__':
    path = './下载'
    m3u8_file_name = 'index.m3u8'
    if not os.path.exists(path):
        print('未找到下载文件夹 现在创建')
        os.makedirs(path)
    session = requests.session()
    page_url = 'https://www.uuoozz.com/movie/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    session = get_cookies(session, page_url, headers)
    movie_url = 'https://www.uuoozz.com/play/1577_1_1.html'
    get_m3u8_source(session, movie_url, headers, path, m3u8_file_name)
    movies_url_list = get_movies_url_list(path, m3u8_file_name)
    cookies = session.cookies
    asyncio.run(download_all_ts(movies_url_list, headers, path, cookies))

