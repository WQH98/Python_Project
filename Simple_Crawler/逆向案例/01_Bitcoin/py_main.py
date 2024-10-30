import requests
import time
import random
import base64

now_time = int(time.time() * 1000)


def encrypt_apikey():
    t = 'a2c903cc-b31e-4547-9299-b6d07b7631ab'
    t1 = t[0: 8]
    t2 = t[8: len(t)]
    t3 = t2 + t1
    return t3


def encrypt_time(t):
    e = str(t + 1111111111111)
    t1 = str(random.randint(1, 9))
    t2 = str(random.randint(1, 9))
    t3 = str(random.randint(1, 9))
    return e + t1 + t2 + t3


url = 'https://www.oklink.com/api/explorer/v2/index/all-chain-order'

params = {
    't': now_time
}

e = encrypt_apikey()
t = encrypt_time(now_time)
api_key = base64.b64encode((e + '|' + t).encode('utf-8')).decode()

headers = {
    'X-Apikey': api_key,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

resp = requests.get(url, params=params, headers=headers)
print(resp.json())

