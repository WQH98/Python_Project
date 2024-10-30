import execjs
import time
import requests

f = open('js代码.js', mode='r', encoding='utf-8')
js_code = f.read()
f.close()
js = execjs.compile(js_code)

# url = 'https://match.yuanrenxue.cn/api/match/1?page=3&m=e8c210321dcfceaf9be5da721e732bc9%E4%B8%A81719681966'
# headers = {
#     # 'Cookie': 'sessionid=b7pjgrp9wrohzh25t49x70wll163oilb;',
#     'Host': 'match.yuanrenxue.com',
#     'Referer': 'http://match.yuanrenxue.com/match/1',
#     'User-Agent': 'yuanrenxue.project',
# }
# resp = requests.get(url, headers=headers)
# print(resp.text)

url = 'https://match.yuanrenxue.cn/api/match/1'

for i in range(1, 6):
    m = js.call('encryptMD5')
    params = {
        'page': str(i),
        'm': m,
    }

    print(params)

    headers = {
        'Cookie': 'sessionid=b7pjgrp9wrohzh25t49x70wll163oilb;',
        'Host': 'match.yuanrenxue.com',
        'Referer': 'http://match.yuanrenxue.com/match/1',
        'User-Agent': 'yuanrenxue.project',
    }

    resp = requests.get(url, params=params, headers=headers)

    print(resp.url)

    print(resp.json())
    # break


