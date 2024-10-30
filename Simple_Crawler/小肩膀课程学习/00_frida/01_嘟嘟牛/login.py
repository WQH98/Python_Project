from hashlib import md5
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64
import time
import requests
import json


def get_sign():
    now_time = str(int(time.time() * 1000))
    data = f'equtype=ANDROID&loginImei=Androidnull&timeStamp={now_time}&userPwd=1234567890&username=15588547880&key=sdlkjsdljf0j2fsjk'
    sign = str(md5(data.encode('utf-8')).hexdigest().upper())
    return sign


def get_data():
    now_time = str(int(time.time() * 1000))
    data = f'{{"equtype":"ANDROID","loginImei":"Androidnull","sign":"{get_sign()}","timeStamp":"{now_time}","userPwd":"1234567890","username":"15588547880"}}'

    des_key = '65102933'
    des_key = str(md5(des_key.encode('utf-8')).hexdigest())
    desKey = bytes.fromhex(des_key)
    des_iv = '32028092'.encode()
    des = DES.new(key=desKey[0:8], mode=DES.MODE_CBC, IV=des_iv)
    bs = data.encode('utf-8')
    bs = pad(bs, 8)
    res = des.encrypt(bs)

    res = base64.b64encode(res).decode()
    return res


def login():
    data = get_data()
    data = json.dumps({"Encrypt": data})
    url = 'http://api.dodovip.com/api/user/login'
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 11; ONEPLUS A6000 Build/RKQ1.201217.002)',
        'Host': 'api.dodovip.com'
    }
    resp = requests.post(url, headers=headers, data=data)
    print(resp.text)

    des_key = '65102933'
    des_key = str(md5(des_key.encode('utf-8')).hexdigest())
    desKey = bytes.fromhex(des_key)
    des_iv = '32028092'.encode()
    des = DES.new(key=desKey[0:8], mode=DES.MODE_CBC, IV=des_iv)

    bs = base64.b64decode(resp.text.encode())
    bs = des.decrypt(bs)
    bs = unpad(bs, 8)
    bs = bs.decode('utf-8')
    print(bs)


if __name__ == '__main__':
    # get_sign()
    login()
