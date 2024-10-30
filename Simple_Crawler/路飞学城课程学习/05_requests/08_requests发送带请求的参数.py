import requests

url = 'http://www.baidu.com/?'

wd = {
    'wd': '测试',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%B5%8B%E8%AF%95&fenlei=256&rsv_pq=0xd06ac352017c8aa2&rsv_t=d2b4VY2XVLCxo7B0%2BnrIsfH99mH%2BE4VcqdTsUBktdrVrf7otY%2BeyGnNZFy8X&rqlang=en&rsv_dl=tb&rsv_enter=1&rsv_sug3=7&rsv_sug1=4&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&inputT=802&rsv_sug4=1245&rsv_sug=1',
}

res = requests.get(url, params=wd, headers=headers)

print(res.content.decode('utf-8'))
