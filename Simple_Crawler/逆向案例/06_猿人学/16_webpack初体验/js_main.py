import requests
import time
import execjs

with open('./btoa.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()

def get_m(now_time):
    js = execjs.compile(js_code)
    return js.call('btoa', now_time)


url = 'https://match.yuanrenxue.cn/api/match/16'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
cookies = {
    'sessionid': '8yqal3j1epppwa4don0u7cds2o846hut;'
}

sum_value = 0

for i in range(1, 6):
    now_time = str(int(time.time()) * 1000)
    params = {
        'page': i,
        'm': get_m(now_time),
        't': now_time
    }

    resp = requests.get(url, params=params, headers=headers, cookies=cookies).json()
    for value in resp['data']:
        sum_value += value['value']

print(sum_value)




'''
r8TRfTCRezhkJMPe371400b29bdaee7c1410dd8e64cc6d5yaKsSyERCt
rMZ7cAm3yctEKSz5038d86f9fce42fb3039c5849d928d1cS76BcD8MGz
iBjwMRijhEQ8n6WTRpZrTjYB4
mtBdmFFMmGd3M4G64pnAEH6Dw
'''
