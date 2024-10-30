from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import json
import requests


def test1(a, b, c):
    if b == 0:
        return a[c:]
    return a[0: b] + a[b + c:]


def test2(data):
    iv = int(data[len(data) - 1], 16) + 9
    key = int(data[iv], 16)
    data = test1(data, iv, 1)
    iv = data[key: key + 8]
    data = test1(data, key, 8)
    key = iv.encode('utf-8')
    iv = iv.encode('utf-8')
    des = DES.new(key=key, mode=DES.MODE_ECB)
    data = bytes.fromhex(data)
    result = des.decrypt(data)
    result = unpad(result, 8).decode('utf-8')
    result = result[:result.rfind('}') + 1]
    print(json.loads(result))


if __name__ == '__main__':
    url = 'https://www.endata.com.cn/API/GetData.ashx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    data = {
        'year': '2024',
        'MethodName': 'BoxOffice_GetYearInfoData'
    }
    resp = requests.post(url, headers=headers, data=data)
    # print(resp.text)
    test2(resp.text)

