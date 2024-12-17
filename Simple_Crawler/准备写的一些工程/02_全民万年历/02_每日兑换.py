import time
import requests
import random

usertoken = ';+:w?Bw,>zi&1:/DGl?Ne$QG~G;1{;FP%2mz39#Os,zo)91AM8H)z#'
deviceid = '4268947'
userid = '2200667'

def exchange():
    url = 'https://c-dapi.qmrl888.com/gcoin/rp.api'

    data = {
        "id": "daily",
        "type": "ali"
    }

    headers = {
        'Host': 'c-dapi.qmrl888.com',
        'app': 'xiaomi',
        'vercode': '50',
        'version': '4.6.1',
        'osver': '11',
        'serverapi': '2',
        'os': 'Android',
        'deviceid': deviceid,
        'userid': userid,
        'usertoken': usertoken,
        'content-type': 'application/json; charset=UTF-8',
        'content-length': '27',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.11.0',
    }

    for i in range(1, 11):
        res = requests.post(url, json=data, headers=headers).json()
        if res['code'] == 200:
            print(f"提现成功 第 {i} 次 {res['result']['rmb'] / 1000} 元")
        else:
            print(f"体现失败 {res['msg']['tip']['msg']}")
            return
        delay_time = random.randint(55, 65)
        print(f"延时 {delay_time} 秒后提现")
        time.sleep(delay_time)


def coin_change(value):
    url = 'https://dapi.qmrl888.com/gcoin/gcoin2Rcoin.api'
    data = {
        'gcoin': value
    }
    headers = {
        'Host': 'dapi.qmrl888.com',
        'app': 'xiaomi',
        'vercode': '50',
        'version': '4.6.1',
        'osver': '11',
        'serverapi': '2',
        'os': 'Android',
        'deviceid': deviceid,
        'userid': userid,
        'usertoken': usertoken,
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.11.0',
    }
    resp = requests.post(url, json=data, headers=headers).json()
    if resp['code'] == 200:
        print(f"使用金币 {value} 成功兑换 {value/2/10000} 元")
    else:
        print("金币换零钱失败")
    return value/2/10000


def get_information():
    coin_a = 0
    url = 'https://dapi.qmrl888.com/gcoin/user.api?app=oppo&userLevel=4379967489&os=Android&verify=default&vip=default&serverApi=2&verCode=53'
    headers = {
        'Host': 'dapi.qmrl888.com',
        'app': 'xiaomi',
        'vercode': '50',
        'version': '4.6.1',
        'osver': '11',
        'serverapi': '2',
        'os': 'Android',
        'deviceid': deviceid,
        'userid': userid,
        'usertoken': usertoken,
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.11.0',
    }
    resp = requests.get(url, headers=headers).json()
    if resp['code'] == 200:
        print('查询信息成功')
        print(f"昨日金币 {resp['result']['yesterdayGcoin']}")
        print(f"今日金币 {resp['result']['todayGcoin']}")
        print(f"当前金币 {resp['result']['gcoin']}")
        print(f"当前零钱 {int(resp['result']['rcoin']) / 1000}")
        if int(resp['result']['gcoin'] / 200) > 0:
            print('开始使用金币换零钱')
            coin_a = coin_change(int(resp['result']['gcoin'] / 200) * 200)
        else:
            print("金币小于200 不够换零钱的")
        if int(resp['result']['rcoin']) / 1000 + coin_a < 0.3:
            print("当前零钱小于0.3 无法提现 直接退出")
            return
        print('开始提现')
        exchange()
    else:
        print('查询信息失败')


if __name__ == '__main__':
    get_information()
