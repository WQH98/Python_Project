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

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = 'https://www.9meiju.cc/mohuankehuan/shandianxiadibaji/1-1.html'
    get_m3u8_url(url)