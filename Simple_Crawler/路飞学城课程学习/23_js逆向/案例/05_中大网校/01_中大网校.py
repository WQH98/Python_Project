'''
    1. 需要访问https://user.wangxiao.cn/apis//common/getImageCaptcha加载验证码
    2. 拿着这个验证码去第三方平台进行识别 获得 正确的验证码
    3. 密码（需要加密） 得到密文
    4. 组织好 数据包发给服务器
    5. 根据服务器返回的内容来判别是否登录成功

    用session来维护cookie比较方便
    session维护的是响应头的set-cookie内容
    对于JavaScript动态加载的cookie session是不维护的
'''
import base64
import json
import requests
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import time


def base64_api(img_b64, typeid):
    """
        在线图像识别使用 返回验证码的值
    """
    data = {"username": 'qq2361125846', "password": 'dzyjs81A', "typeid": typeid, "image": img_b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


session = requests.session()

session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'

'''
    先进入登录页面（用来加载一波cookie） 大部分登录页面是这么做的
    不是为了响应体和源代码 而是为了加载cookie
'''
session.get(url='https://user.wangxiao.cn/login')

'''
    访问https://user.wangxiao.cn/apis//common/getImageCaptcha
    获取验证码
'''

url = 'https://user.wangxiao.cn/apis//common/getImageCaptcha'
session.headers['Referer'] = 'https://user.wangxiao.cn/login'
session.headers['Origin'] = 'https://user.wangxiao.cn'
session.headers['Content-Type'] = 'application/json;charset=UTF-8'
resp = session.post(url)
base64_img = resp.json()['data'].split(',')[1]
with open('验证码.png', mode='wb') as f:
    f.write(base64.b64decode(base64_img))

auth_code = base64_api(base64_img, 1003)

'''
    加密密码
'''
password_time = int(time.time() * 1000)

password = f'19981114wqh{password_time}'
rsa_key = RSA.importKey('-----BEGIN RSA PRIVATE KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB\n-----END RSA PRIVATE KEY-----')
rsa = PKCS1_v1_5.new(key=rsa_key)
password = rsa.encrypt(password.encode('utf-8'))
# 将结果处理成base64 方便进行传输
password = base64.b64encode(password).decode()


'''
    准备登录需要的各种参数
'''
data = {
    'userName': '15588547880',
    'password': password,
    'imageCaptchaCode': auth_code
}

login_url = 'https://user.wangxiao.cn/apis//login/passwordLogin'

resp = session.post(login_url, json=data)
resp_text = resp.json()['data']
print(resp_text)

session.cookies['autoLogin'] = 'true'
session.cookies['userInfo'] = json.dumps(resp_text)
session.cookies['token'] = resp_text['token']
session.cookies['UserCookieName'] = resp_text['userName']
session.cookies['OldUsername2'] = resp_text['userNameCookies']
session.cookies['OldUsername'] = resp_text['userNameCookies']
session.cookies['OldPassword'] = resp_text['passwordCookies']
session.cookies['UserCookieName_'] = resp_text['userName']
session.cookies['OldUsername2_'] = resp_text['userNameCookies']
session.cookies['OldUsername_'] = resp_text['userNameCookies']
session.cookies['OldPassword_'] = resp_text['passwordCookies']
session.cookies[resp_text['userName'] + '_exam'] = resp_text['sign']


'''
    验证登录状态是否可用
'''
list_questions_url = 'https://ks.wangxiao.cn/practice/listQuestions'
data = {
    "practiceType": "2",
    "sign": "jz2",
    "subsign": "467b39463bc6cbc2e7d6",
    "examPointType": "",
    "questionType": "",
    "top": "30"
}
resp = session.post(list_questions_url, json=data)
print(resp.json())
