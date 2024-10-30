import random
import requests
import time
import json


now_time = str(int(time.time() * 1000))

print(now_time)

is_check_url = 'https://hapi.qmrl888.com/v2/gcoin/checkInfo.api'
check_url = 'https://hapi.qmrl888.com/v2/gcoin/check.api'
checkVeGcoin_url = "https://hapi.qmrl888.com/v2/gcoin/checkVeGcoin.api"
preVe_url = "https://dapi.qmrl888.com/app/preVe.api"

headers = {
    'Host': 'hapi.qmrl888.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'deviceid': '3665258',
    'qmsign': 'nwp27IiAodZpUGeYjA1iKCiWScVIiF6lc0UP8EWiXiAXSDO1FuoP0ll/E8QJKfDC',
    'timestamp': now_time,
    'serverapi': '2',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; ONEPLUS A6000 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'osver': '11',
    'vercode': '53',
    'userid': '2200667',
    'usertoken': '4{qv>8mM4$gP}]@)[!}Bd2>R4qG~Y;H2r],YZ5*7F>_VLJZ6Y~b8JJ',
    'qm': '3BdJ3yCADB2r4e57',
    'os': 'Android',
    'app': 'oppo',
    'version': '4.6.4',
    'origin': 'https://he.qmrl888.com',
    'x-requested-with': 'com.aoyi.calendar',
}

preVe_data = {
    "veLocId": "checkVideo"
}

checkVeGcoin_data = {
    "veId": ""
}

resp = requests.get(is_check_url, headers=headers).json()
print(resp)
if resp['code'] == 200:
    print("检查签到成功")
    print(f"已经签到 {resp['result']['checkDay']} 天")
    if resp['result']['todayIsCheck'] == True:
        print("今日未签到")
        if resp['result']['bindWechat'] == True:
            print("已经绑定微信")
        else:
            print("未绑定微信")
        if resp['result']['bindAli'] == True:
            print("已经绑定支付宝")
        else:
            print("未绑定支付宝")
        print("开始签到")
        resp = requests.get(check_url, headers=headers).json()
        print(resp)
        delay_s = random.randint(30, 50)
        print(f"延时 {delay_s} 秒后 开始翻倍")
        time.sleep(delay_s)
        resp = requests.post(preVe_url, headers=headers, json=preVe_data).json()
        print(resp)
        print(f"获取密钥为 {resp['result']['veId']}")
        checkVeGcoin_data["veId"] = resp["result"]["veId"]
        resp = requests.post(checkVeGcoin_url, headers=headers, json=checkVeGcoin_data).json()
        print(resp)
        if resp["code"] == 200:
            print(f"翻倍成功 获得 {resp['result']['text']}")
        else:
            print("翻倍失败")
    else:
        print("今日已签到")
else:
    print("检查签到失败")

