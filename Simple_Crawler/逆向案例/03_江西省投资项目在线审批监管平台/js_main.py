import requests
import execjs
import re

url = 'http://tzxm.jxzwfww.gov.cn/icity/ipro/open/publicity'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}

resp = requests.get(url, headers=headers)
sign = str(re.search('var __signature = "(.*?)";', resp.text).group(1))

url = 'http://tzxm.jxzwfww.gov.cn'

f = open('js.js', mode='r', encoding='utf-8')
js_code = f.read()
f.close()

js = execjs.compile(js_code)
url += js.call('test1', sign)

data = {
    "page": "1",
    "rows": "10",
    "type": "0",
    "year": "2024",
    "projectName": "",
    "flag": "week",
    "projectCode": ""
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Content-Type': 'application/json',
}


resp = requests.post(url, json=data, headers=headers)
print(resp.json())

