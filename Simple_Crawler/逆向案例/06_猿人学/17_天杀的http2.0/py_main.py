import httpx

client = httpx.Client(http2=True)

sum = 0

url = 'https://match.yuanrenxue.cn/api/match/17'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

cookies = {
    'sessionid': 'a9gn1c7360zopx0s2d03ndtn5pgyqt08',
}


for i in range(1, 6):
    url = "https://match.yuanrenxue.cn/api/match/17"
    params = {
        'page': i
    }
    resp = client.get(url, params=params, headers=headers, cookies=cookies).json()
    # print(resp.text)
    for j in range(0, 10):
        sum += resp['data'][j]['value']

print(sum)
