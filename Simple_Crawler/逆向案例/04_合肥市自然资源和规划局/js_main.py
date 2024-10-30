import requests
import execjs
import re
import json


session = requests.session()

url = 'https://zrzyhghj.hefei.gov.cn/xwzx/bsdt/index.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}
'''
    第一次请求 返回消息中有一个cookie   __jsluid_s
    使用js的自运行eval 直接出结果
    返回中携带了 另外一个cookie __jsl_clearance_s
'''
resp = session.get(url, headers=headers)
js_code = re.search('cookie=(.*?);location', resp.text).group(1)
js_clearance = execjs.eval(js_code).split(';')[0].split('=')[1]
session.cookies['__jsl_clearance_s'] = js_clearance

'''
    在第二次的请求中添加第一次请求得到的两个cookie
    返回一段经过ob混淆的代码 将代码分析后写入js文件中
'''
resp = session.get(url, headers=headers)
params = '{' + re.search('go\\({(.*?)\\)</script>', resp.text).group(1)
print("params: ", params)
f = open('./扣js.js', mode='r', encoding='utf-8')
js_code = f.read()
f.close()
js = execjs.compile(js_code)
res = js.call('hash_encode', json.loads(params))
print(res)

'''
    在第三次的请求中 携带第一次得到的cookie __jsluid_s
    在第二次请求获得的代码中 找到一些返回的数据 经过js代码运行后
    得到改变后的第二个cookie __jsl_clearance_s
    带上两个cookie 可以得到正确的结果
'''
session.cookies['__jsl_clearance_s'] = res
resp = session.get(url, headers=headers)
resp.encoding = 'utf-8'
print(resp.text)

