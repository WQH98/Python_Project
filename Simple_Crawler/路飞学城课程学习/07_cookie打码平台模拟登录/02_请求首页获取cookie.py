import requests

url = 'https://xueqiu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}

response = requests.get(url, headers=headers)
cookies = response.cookies
print(cookies)
print(dict(cookies))

url = 'https://xueqiu.com/statuses/hot/listV3.json?page=2&last_id=285618131'
response = requests.get(url, headers=headers, cookies=cookies)
print(response)

