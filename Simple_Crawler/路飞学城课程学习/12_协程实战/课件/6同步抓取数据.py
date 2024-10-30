import time

import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

def get_movie_url():
    '''
    抓取电影页面中详情页url的函数
    :return: ur_list
    '''
    url = 'https://movie.douban.com/chart'
    res = requests.get(url, headers=headers)
    text = res.text
    tree = etree.HTML(text)
    # 获取页面中电影详情页的url
    url_list = tree.xpath('//*[@id="content"]/div/div[1]/div/div/table/tr/td[2]/div/a/@href')
    return url_list

def get_movie_detail(detail_url):
    res = requests.get(detail_url, headers=headers)
    text = res.text
    tree = etree.HTML(text)
    # 抓取详情页的数据
    detail_con = tree.xpath('//*[@id="content"]/h1/span[1]//text()')
    print(detail_con)
    return detail_con


if __name__ == '__main__':
    t1 = time.time()
    url_list = get_movie_url()
    # get_movie_detail('https://movie.douban.com/subject/35073886/')
    for url in url_list:
        get_movie_detail(url)
    print(time.time()-t1)


