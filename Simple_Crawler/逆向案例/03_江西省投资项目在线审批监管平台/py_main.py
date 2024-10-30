import requests
import re
import random
import time

url = 'http://tzxm.jxzwfww.gov.cn/icity/ipro/open/publicity'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}

resp = requests.get(url, headers=headers)
sign = str(re.search('var __signature = "(.*?)";', resp.text).group(1))

chars = "0123456789abcdef"

key = ""
keyIndex = -1
for i in range(6):
    c = sign[keyIndex+1]
    key += c
    keyIndex = chars.find(c)
    if keyIndex < 0 or keyIndex >= len(sign):
        keyIndex = i


now_time = str(int(time.time() * 1000))
timestamp = str(random.randint(1000, 9999)) + '_' + key + '_' + now_time

tkey = ''
tkeyIndex = -1
for i in range(6):
    c = timestamp[tkeyIndex + 1]
    tkey += c
    tkeyIndex = chars.find(c)
    if tkeyIndex < 0 or tkeyIndex >= len(timestamp):
        tkeyIndex = i


url = 'http://tzxm.jxzwfww.gov.cn/icity/api-v2/jxtzxm.app.icity.ipro.IproCmd/getDisplayListByPage'

params = {
    's': sign,
    't': timestamp,
    'o': tkey,
}

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

resp = requests.post(url, json=data, headers=headers, params=params)
print(resp.json())


