import asyncio
import time
import aiohttp

import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

async def get_movie_url():
    '''
    抓取电影页面中详情页url的函数
    :return: ur_list
    '''
    url = 'https://movie.douban.com/chart'
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            text = await resp.text()
            tree = etree.HTML(text)
            # 获取页面中电影详情页的url
            url_list = tree.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[2]/div/a/@href')
    return url_list

async def get_movie_detail(detail_url):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(detail_url) as resp:
            text = await resp.text()
            tree = etree.HTML(text)
            # 抓取详情页的数据
            detail_con = tree.xpath('//*[@id="content"]/h1/span[1]//text()')
            print(detail_con)
    return detail_con


if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()
    url_list = loop.run_until_complete(get_movie_url())  # 获取返回详情页url的列表
    tasks = [get_movie_detail(url) for url in url_list]  # 创建task任务
    loop.run_until_complete(asyncio.gather(*tasks))
    print(time.time()-t1)


