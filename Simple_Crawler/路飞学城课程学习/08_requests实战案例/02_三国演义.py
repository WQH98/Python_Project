import os.path
import random
import time
import requests
from lxml import etree


def get_four_url():
    ret_urls = []
    url = "https://www.shicimingju.com/bookmark/sidamingzhu.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    response = requests.get(url, headers=headers).content.decode()
    tree = etree.HTML(response)
    urls = tree.xpath('//div[@class="book-item"]/a/@href')
    for url in urls:
        ret_urls.append("https://www.shicimingju.com/" + url)
    return ret_urls


def get_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    try:
        response = requests.get(url, headers=headers).content.decode()
        tree = etree.HTML(response)
        path = tree.xpath('//div[@class="card bookmark-list"]/h1/text()')[0]
        path1 = f'./四大名著文章下载/{path}'
        if not os.path.exists(path1):
            print(f"未找到{path}文件夹 现在创建文件夹")
            os.mkdir(path1)
        book_urls = tree.xpath('//div[@class="book-mulu"]/ul/li/a/@href')
        urls = []
        for book_url in book_urls:
            urls.append("https://www.shicimingju.com/" + book_url)
        print(f"开始爬取{path}")
        return urls, path1
    except:
        print("爬取出错 暂停5秒重新爬取")
        time.sleep(5)
        get_url(url)


def download_book(url, path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
    }
    try:
        response = requests.get(url, headers=headers).content.decode()
        tree = etree.HTML(response)
        chapter_name = tree.xpath('//div[@class="card bookmark-list"]/h1/text()')[0]
        txts = tree.xpath('//div[@class="chapter_content"]/p/text()')
        print(f'start {chapter_name}')
        chapter_text = ""
        for txt in txts:
            chapter_text += "    " + txt.strip() + "\n"
        with open(f'{path}/{chapter_name}.txt', "w", encoding="utf-8") as f:
            f.write(chapter_text)
    except:
        print("爬取出错 暂停5秒重新爬取")
        time.sleep(5)
        download_book(url, path)


if __name__ == "__main__":
    four_urls = get_four_url()
    for four_url in four_urls:
        urls, path = get_url(four_url)
        for url in urls:
            download_book(url, path)
            time.sleep(random.randint(5, 7))
