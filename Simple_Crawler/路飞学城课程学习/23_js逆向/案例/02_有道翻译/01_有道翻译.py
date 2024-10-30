import base64
import hashlib
import requests
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

url = 'https://dict.youdao.com/webtranslate'

time = str(int(time.time() * 1000))

s = f'client=fanyideskweb&mysticTime={str(time)}&product=webfanyi&key=fsdsogkndfokasodnaso'
sign = hashlib.md5(s.encode('utf-8')).hexdigest()

data = {
    'i': 'hello world',
    'from': 'auto',
    'to': 'auto',
    'useTerm': 'false',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': sign,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': str(time),
    'keyfrom': 'fanyi.web',
    'mid': '1',
    'screen': '1',
    'model': '1',
    'network': 'wifi',
    'abtest': '0',
    'yduuid': 'abcdefg',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=1103626094@2001:250:1409:2105:597e:2bf5:da75:e5d8; OUTFOX_SEARCH_USER_ID_NCOO=2119093129.7009878',
    'Host': 'dict.youdao.com',
    'Origin': 'https://fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
}

resp = requests.post(url, data=data, headers=headers)
print(resp.text)

'''
t = ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl
o = ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4
'''

decode_key = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
decode_iv = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'
key = hashlib.md5(decode_key.encode('utf-8')).digest()
iv = hashlib.md5(decode_iv.encode('utf-8')).digest()
aes_en = AES.new(key, AES.MODE_CBC, iv)
data_new = base64.urlsafe_b64decode(resp.text)
result = aes_en.decrypt(data_new)
result = unpad(result, 16)
result = result.decode('utf-8')
print(result)
