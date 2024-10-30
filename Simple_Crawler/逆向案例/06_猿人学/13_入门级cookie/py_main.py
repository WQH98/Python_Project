import requests
import re
import execjs

url = 'https://match.yuanrenxue.cn/match/13'
sum = 0
session = requests.session()

headers = {
    'User-Agent': 'yuanrenxue.project',
}
session.cookies['sessionid'] = 'a9gn1c7360zopx0s2d03ndtn5pgyqt08'
resp = session.get(url, headers=headers)
print(resp.text)
cookies_js = re.findall("document.cookie=(.*?)\+';path=/';", resp.text)[0]
print(cookies_js)
cookies = execjs.eval(cookies_js)
yuanrenxue_cookie = cookies.split('=')[1]
print(yuanrenxue_cookie)
session.cookies['yuanrenxue_cookie'] = yuanrenxue_cookie

for i in range(1, 6):
    url = "https://match.yuanrenxue.cn/api/match/13"
    params = {
        'page': i
    }
    resp = session.get(url, params=params, headers=headers).json()
    # print(resp.text)
    for j in range(0, 10):
        sum += resp['data'][j]['value']

print(sum)
