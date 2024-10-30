import uuid
import random
import base64
from Crypto.Cipher import DES3
import requests
import hashlib


def des3(data_string):
    BS = 8
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    # DES3的MODE_CBC模式只有前24位有效
    key = b"appapiche168comappapiche168comap"[0: 24]
    iv = b"appapich"

    plaintext = pad(data_string).encode("utf-8")

    # 使用MODE_CBC创建cipher
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    result = cipher.encrypt(plaintext)
    return base64.b64encode(result).decode("utf-8")


def md5(data_string):
    obj = hashlib.md5()
    obj.update(data_string.encode("utf-8"))
    return obj.hexdigest()


def run():
    username = "15588588888"
    password = "123456abcd"

    imei = str(uuid.uuid4())
    nano_time = random.randint(5136066335773, 7136066335773)
    device_id = "397671"
    udid = des3(f"{imei}|{nano_time}|{device_id}")

    data = "W@oC!AH_6Ew1f6%8"
    datas = {
        "_appid": "atc.android",
        "appversion": "3.42.0",
        "channelid": "csy",
        "pwd": md5(password),
        "udid": udid,
        "username": username
    }

    result = "".join(["{}{}".format(key, datas[key]) for key in sorted(datas.keys())])
    un_sign_string = f"{data}{result}{data}"
    sign = md5(un_sign_string).upper()
    datas["_sign"] = sign

    url = "https://dealercloudapi.che168.com/tradercloud/sealed/login/login.ashx"
    res = requests.post(url=url, data=datas)
    print(res.status_code)
    print(res.text)


if __name__ == "__main__":
    run()
