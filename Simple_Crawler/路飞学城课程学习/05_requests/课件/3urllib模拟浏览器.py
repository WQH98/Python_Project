import urllib.request
url = 'https://www.baidu.com/s?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
kw = {
    'wd': '迪丽热巴'
}
new_url = url + urllib.parse.urlencode(kw)
# print(new_url)
# 构造模拟浏览器请求对象  （开始装了。。。）
request = urllib.request.Request(url=new_url, headers=headers)
res = urllib.request.urlopen(request)
# 写入到html中
with open('dlrb.html', 'w') as f:
    f.write(res.read().decode('UTF-8'))