import requests

session = requests.session()

login_url = 'https://match.yuanrenxue.cn/api/login'

login_data = {
    'username': 'qq2361125846',
    'password': '19981114wqh'
}

login_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

session.post(url=login_url, data=login_data, headers=login_headers)

jssm_url = 'https://match.yuanrenxue.cn/jssm'

data_headers = {
    'Content-Length': '0',
    'Accept': '*/*',
    'Referer': 'https://match.yuanrenxue.cn/match/3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

session.headers = data_headers

data_url = 'https://match.yuanrenxue.cn/api/match/3'

datas = {}

for i in range(1, 6):
    params = {
        'page': i
    }

    session.post(url=jssm_url)
    resp = session.get(data_url, params=params).json()

    for value in resp['data']:
        if value['value'] in datas:
            datas[value['value']] += 1
        else:
            datas[value['value']] = 0


max_count = 0
max_data = ""
for data in datas:
    if datas[data] > max_count:
        max_count = datas[data]
        max_data = data

print(max_data, max_count)


