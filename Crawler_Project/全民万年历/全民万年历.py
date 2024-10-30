import time
import requests

url = 'https://c-dapi.qmrl888.com/gcoin/rp.api'

data = {
  "id": "daily",
  "type": "ali"
}

headers = {
    'Host': 'c-dapi.qmrl888.com',
    'app': 'xiaomi',
    'vercode': '43',
    'version': '4.4.4',
    'osver': '14',
    'serverapi': '2',
    'os': 'Android',
    'deviceid': '2156100',
    'userid': '2200667',
    'usertoken': '+.>~!oA#+WS7DL.~n!Zph1~qB:Ar&9g[z}5_l6N,F%)2>)A;O@UQ3[',
    'content-type': 'application/json; charset=UTF-8',
    'content-length': '27',
    'accept-encoding': 'gzip',
    'user-agent': 'okhttp/4.11.0',
}

for i in range(0, 10):
    res = requests.post(url, json=data, headers=headers)
    print(res.json())
    time.sleep(60)


