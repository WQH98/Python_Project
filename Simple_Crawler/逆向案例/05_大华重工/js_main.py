import requests
import execjs
import re


'''
    组装头部与url
'''
session = requests.Session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
url = 'https://www.lydh.com/jituan/'


'''
    第一次请求以后返回中携带一个cookie
    返回一段混淆的代码 代码中设置了另外一个cookie
'''
resp = session.get(url, headers=headers, verify=False)
with open('测试js.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()


'''
    通过给的arg1参数 计算混淆代码出的cookie
'''
arg1 = re.findall("var arg1='(.*?)';", resp.text)[0]
js = execjs.compile(js_code)
acw_sc__v2 = js.call("_0x4818", str(arg1))


'''
    使用js计算 得到cookie 设置进session 
'''
session.cookies['acw_sc__v2'] = acw_sc__v2


'''
    携带两个cookie 再次进行get 即可获得数据
'''
resp = session.get(url, headers=headers)
resp.encoding = "utf-8"
print(resp.text)
