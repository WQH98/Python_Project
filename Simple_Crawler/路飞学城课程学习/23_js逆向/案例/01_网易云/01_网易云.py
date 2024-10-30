# 如果js代码中含有中文 则引入以下代码
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

import execjs
import requests

data = {
    'ids': '[2146228675]',
    'level': 'standard',
    'encodeType': 'aac',
    'csrf_token': ''
}

f = open('01_网易.js', mode='r', encoding='utf-8')
js_code = f.read()
f.close()

js = execjs.compile(js_code)
r = js.call('fn', data)

real_data = {
    'params': r['encText'],
    'encSecKey': r['encSecKey']
}

print(real_data)

url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'referer': 'https://music.163.com/',
}

resp = requests.post(url=url, data=real_data, headers=headers)

print(resp.status_code)
print(resp.text)


