import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
}

res = requests.get('https://www.linovelib.com/novel/2547/123015.html', headers=headers)
data = res.content.decode('utf-8')
with open('./02_requests请求逆向.html', 'w', encoding='utf-8') as f:
    f.write(data)
print(data)
