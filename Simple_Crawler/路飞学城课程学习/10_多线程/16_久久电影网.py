import requests
import re

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}


def get_html():
    session.get('https://www.99meijutt.com/', headers=headers, verify=False)
    session.get('https://www.baidu.com/', headers=headers)
    # 请求电影网址
    url = 'https://www.99meijutt.com/play/103594-0-0.html'
    res = session.get(url, headers=headers)
    res.encoding = 'utf-8'
    data = res.text
    with open('16_久久电影网.html', 'w', encoding='utf-8') as f:
        f.write(data)


def get_first_m3u8_url():
    with open('16_久久电影网.html', 'r', encoding='utf-8') as f:
        data = f.read()
    first_m3u8_url = re.search('now="(.+?index.m3u8)"', data).group(1)
    return first_m3u8_url


def get_first_m3u8_url_html(first_m3u8_url):
    res = session.get(first_m3u8_url, headers=headers, verify=False)
    with open('16_first_m3u8_url.txt', 'wb') as f:
        f.write(res.content)


def get_second_m3u8_url():
    with open('16_first_m3u8_url.txt', 'r', encoding='utf-8') as f:
        data = f.read()
    second_m3u8_url = re.search('(.+?.m3u8)', data).group(1)
    return second_m3u8_url


def get_second_m3u8_url_html(second_m3u8_url):
    res = session.get(second_m3u8_url, headers=headers, verify=False)
    with open('16_second_m3u8_url.txt', 'wb') as f:
        f.write(res.content)


if __name__ == '__main__':
    # get_html()
    # first_m3u8_url = get_first_m3u8_url()
    # get_first_m3u8_url_html(first_m3u8_url)
    second_m3u8_url = get_second_m3u8_url()
    get_second_m3u8_url_html(second_m3u8_url)

