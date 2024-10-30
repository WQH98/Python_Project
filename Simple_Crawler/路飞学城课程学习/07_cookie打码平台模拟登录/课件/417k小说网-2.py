import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
# 账号验证的url地址
url = 'https://passport.17k.com/ck/user/login'
# post请求所携带的表单数据
form_data = {
    'loginName': '17346570232',
    'password': 'xlg17346570232'
}
# 实例化session对象 进行会话保持
sess = requests.Session()
sess.post(url, headers=headers, data=form_data)
# 登陆以后访问的url
url = 'https://user.17k.com/www/bookshelf/read.html'
res = sess.get(url, headers=headers)
print(res.content.decode())