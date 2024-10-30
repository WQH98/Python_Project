import os.path
import requests
import re
from urllib.parse import urljoin


def get_m3u8_url(url):
    '''
    抓取页面中的index.m3u8的文件数据 写入到本地index.m3u8文件并返回m3u8url地址
    :param url: 页面的url（要抓取的视频的页面url）
    :return: url
    '''
    res = requests.get(url, headers=headers)
    data = res.content.decode()  # 抓取页面内容

    # 这是抓取第一次的index.m3u8的地址
    index_m3u8_url = re.search('"url":"(.+?index.m3u8)"', data).group(1).replace('\\', '')

    # 进行请求  获取第二次index.m3u8的url地址
    res = requests.get(index_m3u8_url, headers=headers)
    data = res.content.decode()  # 抓取页面内容
    # 拼接第二次请求的m3u8文件地址
    # print(index_m3u8_url.rsplit('/', 1)[0]+'/'+data.split('/', 3)[-1].strip())
    index_m3u8_url = urljoin(index_m3u8_url, data.split('/', 3)[-1]).strip()
    # 请求第二个index.m3u8地址，当前返回的内容就是咱们真正获取ts文件的url
    res = requests.get(index_m3u8_url, headers=headers)
    data = res.content.decode()  # 抓取页面内容
    with open('index.m3u8', 'w', encoding='UTF-8') as f:
        f.write(data)
    return index_m3u8_url


def dowload_one_m3u8(url, i, path):
    '''
    下载单个ts文件的函数
    :param url: 要下载ts的url地址
    :param i: 当前的文件的名称  也就是i的循环自增
    :param path: 当前下载后ts所需要存储的路径
    :return:
    '''
    res = requests.get(url, headers=headers)
    print(url, '正在下载')
    # 拼接下载文件的路径及下载后ts的文件名称
    file_path = os.path.join(path, str(i) + '.ts')
    # 进行下载写入
    with open(file_path, 'wb') as f:
        f.write(res.content)

def download_all_m3u8(path, filename='index.m3u8'):
    '''
    下载所有的m3u8的里面的ts文件
    :param path: 存储下载ts文件的文件夹
    :param filename: m3u8的文件名称
    :return:
    '''
    # 读取index.m3u8文件  以列表形式返回每一行
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
    # 判断 当前存储ts的文件目录是否存在 不存在则创建
    if not os.path.exists(path):
        os.mkdir(path)
    # print(lines)
    # 循环读取每一行数据
    i = 0
    for line in lines:
        # 获取所有要下载的ts的url地址  不以#作为开头
        if line.startswith('#'):
            continue
        # print(line)
        # 进行下载处理
        url = line.strip()  # 去除请求的url中可能包含的其他的字符
        dowload_one_m3u8(url, i, path)
        i += 1

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = 'https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-1.html'
    get_m3u8_url(url)
    path = 'ts'  # 下载所有ts的文件的路径
    download_all_m3u8(path)