import requests
from lxml import etree
import execjs

session = requests.Session()

login_url = 'http://shanzhi.spbeen.com/login/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}

resp = session.get(login_url, headers=headers)
tree = etree.HTML(resp.text)
token = tree.xpath('//form[@id="login_button"]/input/@value')

f = open('扣js.js', mode='r', encoding='utf-8')
js_code = f.read()
f.close()

js = execjs.compile(js_code)
new_password = js.call('doLogin')

data = {
    'username': 'test1234567890',
    'password': new_password,
    'csrfmiddlewaretoken': token
}

resp = session.post(login_url, headers=headers, data=data)
print(resp.text)
