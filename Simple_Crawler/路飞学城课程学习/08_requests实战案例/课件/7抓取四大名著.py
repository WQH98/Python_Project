import os.path
import random
import time

import requests
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

def get_html(url):
    '''
    根据url请求返回tree对象
    :return:
    '''
    res = requests.get(url, headers=headers)
    text = res.content.decode()
    tree = etree.HTML(text)
    return tree

def get_books(tree):
    '''
    根据传递进来的tree对象进行xpath处理返回书名称以及书的url  {'三国演义':http://asdadsdd}
    :param tree:
    :return: {'三国演义':http://asdadsdd}
    '''
    a_list = tree.xpath('//div[@class="book-item"]/h3/a')
    book = {}  # 存储书名称以及书的url  {'三国演义':http://asdadsdd}
    for a in a_list:
        # 获取当前书的url
        href = a.xpath('./@href')[0]
        # 获取四大名著书的名称
        book_name = a.xpath('./text()')[0]
        # 存储成字典
        book[book_name] = 'https://www.shicimingju.com' + href
    # print(book)
    return book

def get_book_mulu(books_tree):
    '''
    处理书里面章节的
    :param books_tree: 三国演义或者红楼梦等书的请求返回的tree对象
    :return: dict {'第一回合...': 'http://sssss',...}
    '''
    # 获取章节名称和url
    li_list = books_tree.xpath('//div[@class="book-mulu"]/ul/li')
    # print(li_list)
    book_mulus= {}
    for li in li_list:
        # 获取章节的url地址
        href = 'https://www.shicimingju.com' + li.xpath('./a/@href')[0]
        # 获取章节名称
        title = li.xpath('./a/text()')[0]
        book_mulus[title] = href
    return book_mulus


def get_mulu_contnets(chapter, mulu_tree):
    '''
    获取章节里面的内容
    :param chapter: 章节的名称
    :param mulu_tree: 章节的tree对象
    :return: {'章节名称'： 章节内容}
    '''
    mulu_contents = mulu_tree.xpath('//div[@class="card bookmark-list"]//text()')
    return {chapter: mulu_contents}

def save_book(book_name, mulu_contents):
    '''
    根据书名，章节名称，里面的书的内容进行下载
    :param book_name: 书名
    :param mulu_contents: {'章节名称': ['章节内容']}
    :return:
    '''
    # 判断书的目录是否存在 不存在则创建
    if not os.path.exists(book_name):
        os.mkdir(book_name)
    # 循环获取章节名称
    for mulu in mulu_contents:
        # 拼凑写入书的名称和章节名称的路径
        path = os.path.join(book_name, mulu+'.text')
        with open(path, 'a', encoding='UTF-8') as f:
            f.writelines(mulu_contents[mulu])
        print(f'【{book_name}】【{mulu}章节】下载成功！')



if __name__ == '__main__':
    # 四大名著的总url
    url = 'https://www.shicimingju.com/bookmark/sidamingzhu.html'
    books = get_books(get_html(url))  # 请求四大名著总的url
    for book_name in books:  # 循环拿到四大名著的书名
        time.sleep(random.randint(1,3))
        href = books[book_name]  # 获取四大名组的书的url地址
        # 循环章节名称和url的字典  拿到对应的章节名称和url
        for mulu, url in get_book_mulu(get_html(href)).items():  # 进程书的url的请求
            # 请求章节名称的url 获取内容
            # 书的章节对于的书中的内容
            time.sleep(random.randint(1, 3))
            mulu_contents = get_mulu_contnets(mulu, get_html(url))
            # 将书进行下载
            save_book(book_name, mulu_contents)
