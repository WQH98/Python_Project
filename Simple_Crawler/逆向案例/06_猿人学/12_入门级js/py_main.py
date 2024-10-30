import base64
import requests

url = "https://match.yuanrenxue.cn/api/match/12"

sum = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'Cookie': 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1719026446; m=d134ed1036d13e503f225045d5d199e5|1719026487000; Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1718109250,1719026532; Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3=1719026532; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1719026562; qpfccr=true; no-alert3=true; tk=-3373964463301196540; sessionid=sovw8cxq3vs22agwxtowrrxfqj1x621e; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1719037160; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1719037160'
}

for i in range(1, 6):
    params_m = ('yuanrenxue' + f'{i}').encode()
    params_m = base64.b64encode(params_m).decode()
    params = {
        'page': i,
        'm': params_m
    }
    resp = requests.get(url, params=params, headers=headers).json()
    for j in range(0, 10):
        sum += resp['data'][j]['value']


print(sum)
