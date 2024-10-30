import requests
import time
import execjs


now_time = int(time.time() * 1000)
f = open('./扣js.js', mode='r', encoding='utf-8')
js_code = f.read()
f.close()
js = execjs.compile(js_code)
api_key = js.call('getApiKey')

url = 'https://www.oklink.com/api/explorer/v2/index/all-chain-order'

params = {
    't': now_time
}

headers = {
    'X-Apikey': api_key,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

resp = requests.get(url, params=params, headers=headers)
print(resp.json())

