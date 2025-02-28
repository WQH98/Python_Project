import requests

gostc_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJDb2RlIjoiOTY3NzI5YTEtOWQ3OC00ZTA3LWIzZjItZjIxYzliOTVjNGQyIiwiRGF0YSI6eyJhZG1pbiI6IjIifSwiZXhwIjoxNzQwODc4NjUzLCJqdGkiOiI5Njc3MjlhMS05ZDc4LTRlMDctYjNmMi1mMjFjOWI5NWM0ZDIiLCJpYXQiOjE3NDAyNzM4NTMsImlzcyI6Imdvc3RjIiwibmJmIjoxNzQwMjczODUzLCJzdWIiOiI5Njc3MjlhMS05ZDc4LTRlMDctYjNmMi1mMjFjOWI5NWM0ZDIifQ.3IUcG-KSa1oDZJlT9mwtNPxFZFIptSwqjpPX0PlvOp8"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-length": "0",
    "origin": "https://gost.sian.one",
    "referer": "https://gost.sian.one/dashboard",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Microsoft Edge";v="133", "Chromium";v="133"',
    "token": gostc_token,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0"
}


def check_in(token):
    check_in_url = "https://gost.sian.one/api/v1/auth/checkin"
    headers["token"] = token
    resp = requests.post(check_in_url, headers=headers)
    if resp.json()["code"] == 1:
        print(resp.json()["msg"])
    else:
        print("签到成功")


def get_user_info(token):
    userinfo_url = "https://gost.sian.one/api/v1/auth/userInfo"
    headers["token"] = token
    resp = requests.post(userinfo_url, headers=headers).json()
    checkinAmount = resp["data"]["checkinAmount"]
    if checkinAmount == '0':
        print(resp["data"]["account"] + " " + "尚未签到，开始签到")
        return 0
    else:
        print(resp["data"]["account"] + " " + "今日已签到，今日签到积分为:" + checkinAmount + "，总积分为：" + resp["data"]["amount"])
        return 1


if __name__ == '__main__':
    res = get_user_info(gostc_token)
    if res == 0:
        check_in(gostc_token)
        get_user_info(gostc_token)



