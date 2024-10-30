import os.path
import random
import time

import requests
from lxml import etree

def get_img(url):
    '''
    https://www.qqtn.com/tp/meinvtp_1.html
    https://www.qqtn.com/tp/meinvtp_2.html
    https://www.qqtn.com/tp/meinvtp_3.html
    https://www.qqtn.com/tp/meinvtp_4.html
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    # data = res.content.decode('GBK')
    # 自动获取解码格式
    res.encoding = res.apparent_encoding
    data = res.text
    # print(data)
    tree = etree.HTML(data)
    url_list = tree.xpath('//ul[@class="g-gxlist-imgbox"]/li/a/img/@src')
    # print(url_list)
    # 图片下载的路径
    path = 'img'
    # 判断下载的文件夹是否存在
    if not os.path.exists(path):
        os.mkdir(path)
    # i = 0
    for url in url_list:
        print(url)
        # 进行图片的请求
        res = requests.get(url, headers=headers)
        # 开始进行下载
        with open(os.path.join(path, str(random.randint(1,1000000))+'.jpg'), 'wb') as f:
            f.write(res.content)
        # i += 1
        time.sleep(0.5)

# url = 'https://www.qqtn.com/wm/meinvtp_1.html'
for i in range(1, 6):
    url = f'https://www.qqtn.com/tp/meinvtp_{i}.html'
    print(url)
    get_img(url)
    time.sleep(2)