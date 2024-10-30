import base64
import json
import requests
def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


if __name__ == "__main__":
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    # 请求验证码的url
    code_url = 'https://so.gushiwen.cn/RandCode.ashx'
    res = requests.get(code_url, headers=headers)
    with open('yzm.jpg', 'wb') as f:
        f.write(res.content)
    img_path = "yzm.jpg"
    # 请求验证码
    result = base64_api(uname='luckyboyxlg', pwd='17346570232', img=img_path, typeid=3)
    print(result)
    login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    form_data = {
        '__VIEWSTATE': 'z60XXxSct8V61abZutBSpakMWslNZHaMddtZsymqIsoNpV1OkLO4Bf + p6aqfB+s4YL/lFHTo2V2ZvU2SmuD6IkDdfYMwgI0Iyo+aqrczD4H81gzM6Bmjf+zrDd + LitV9T50V4zExQ/s7WNB+YKuAiVphPOw=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '793390457@qq.com',
        'pwd': 'xlg17346570232',
        'code': result,
        'denglu': '登录',
    }
    res = requests.post(login_url, headers=headers, data=form_data)
    print(res.content.decode())