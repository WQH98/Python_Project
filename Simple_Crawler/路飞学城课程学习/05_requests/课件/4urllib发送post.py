import urllib.request
import json
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
data = urllib.parse.urlencode(form_data).encode('UTF-8')
request = urllib.request.Request(url=url, data=data,headers=headers)
res = urllib.request.urlopen(request)
print(res.getcode())
# 处理成json字符串
print(json.loads(res.read().decode('UTF-8')))

# 练习
# 将当前请求改为requests