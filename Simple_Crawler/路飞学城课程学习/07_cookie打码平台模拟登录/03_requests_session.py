import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}

# 先访问首页 获取到cookie
session = requests.Session()    # 创建一个session对象
main_url = 'https://xueqiu.com/'
# 这里请求的目的只有一个 就是拿到响应的cookie
res = session.get(main_url, headers=headers)

# 访问异步加载的地址 携带着cookie过去
url = 'https://xueqiu.com/statuses/hot/listV3.json?page=2&last_id=285618131'
res = session.get(url, headers=headers)
print(res)
print(res.json())


