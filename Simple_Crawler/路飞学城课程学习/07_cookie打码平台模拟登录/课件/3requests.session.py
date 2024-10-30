import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# 首页的url
url = 'https://xueqiu.com/'
sess = requests.Session()  # 实例化session
sess.get(url, headers=headers)  # 请求当前的目的是为了拿到服务器端响应的cookie
url = 'https://xueqiu.com/statuses/hot/listV2.json?since_id=-1&max_id=384373&size=15'
res = sess.get(url, headers=headers)
print(res.json())