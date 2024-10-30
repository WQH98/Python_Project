import os.path
import random
import time

import requests
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
'''
https://www.pkdoutu.com/photo/list/?page=3
https://www.pkdoutu.com/photo/list/?page=1
'''
for i in range(1,2):
    url = f'https://www.pkdoutu.com/photo/list/?page={i}'
    print(f'抓取{url}页数据')
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    tree = etree.HTML(res.text)
    # 抓取图片
    img_list = tree.xpath('//img[@referrerpolicy="no-referrer"]/@data-original')
    # print(img_list)
    for url in img_list:
        # 请求图片url
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