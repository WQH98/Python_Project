import math
import requests
import pywasm
import time
import random

def get_m():
    now_time = int(time.time())
    t1 = int(now_time / 2)
    t2 = int(now_time / 2 - math.floor(random.random() * 50 + 1))
    wm = pywasm.load('./main.wasm')
    m = wm.exec('encode', [t1, t2])
    m = str(m) + '|' + str(t1) + '|' + str(t2)
    return m


wasm_url = 'https://match.yuanrenxue.cn/static/match/match15/main.wasm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
resp = requests.get(wasm_url, headers=headers)
with open('main.wasm', mode='wb') as f:
    f.write(resp.content)

sum_value = 0

for i in range(1, 6):
    url = 'https://match.yuanrenxue.cn/api/match/15'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    params = {
        'm': get_m(),
        'page': i
    }
    cookies = {
        'sessionid': 'zn0srqzy3o2gae9autjak0id1ca3chos;'
    }
    resp = requests.get(url, params=params, headers=headers, cookies=cookies).json()
    for value in resp['data']:
        sum_value += value['value']


print(sum_value)

