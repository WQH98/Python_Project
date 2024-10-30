import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# 首页的url
url = 'https://xueqiu.com/'
res1 = requests.get(url, headers=headers)
# print(res1.status_code)
# print(res1.cookies)
# 获取第一次请求服务器端响应的cookie
cookies = dict(res1.cookies)
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=384373&size=15'
# 请求携带cookie
res = requests.get(url, headers=headers, cookies=cookies)
print(res.status_code)
print(res.json())
