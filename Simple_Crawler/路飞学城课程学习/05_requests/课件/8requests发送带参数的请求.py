import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
kw = {
    'wd': '迪丽热巴'
}
url = 'https://www.baidu.com/s?'

res = requests.get(url, params=kw, headers=headers)
print(res.content.decode('UTF-8'))