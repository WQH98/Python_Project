import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi&sign=bd68349d763bf521'
# post 携带表单数据
form_data = {
    'from': 'zh',
    'to': 'en',
    'q': 'lucky 我爱你'
}
# 发送post请求
res = requests.post(url, headers=headers, data=form_data)
print(res.json())