import requests
from notify import send


token = 'klqt0wakwvsosy8ybbvsnra80sr09ww7'

headers = {
    'xweb_xhr': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c04)XWEB/11237',
    'x-dts-token': token,
    'content-type': 'application/json',
    'accept': '*/*',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://servicewechat.com/wx6b6c5243359fe265/157/page-frame.html',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
}


def sign():
    global send_msg
    url = "https://www.kozbs.com/demo/wx/home/sign?userId=198350"
    resp = requests.get(url, headers=headers).json()
    msg = f"签到 {resp['errmsg']}\n"
    print(msg, end="")
    send_msg += msg


def share():
    global send_msg
    url = "https://www.kozbs.com/demo/wx/user/addIntegralByShare?userId=198350"
    resp = requests.get(url, headers=headers).json()
    msg = f"分享 {resp['errmsg']}\n\n"
    print(msg, end="")
    send_msg += msg


def get_balance():
    global send_msg
    url = "https://www.kozbs.com/demo/wx/home/signDay?userId=198350"
    resp = requests.get(url, headers=headers).json()
    msg = f"剩余积分 {resp['data']['integral']}\n"
    print(msg, end="")
    send_msg += msg


if __name__ == '__main__':
    global send_msg
    send_msg = ""
    msg = "开始签到\n"
    print(msg, end="")
    send_msg += msg
    sign()

    msg = "开始分享\n"
    print(msg, end="")
    send_msg += msg
    share()

    get_balance()

    send("植白说-通知", send_msg)

