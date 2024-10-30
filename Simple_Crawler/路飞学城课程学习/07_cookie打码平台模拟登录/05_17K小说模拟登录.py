import requests


url = 'https://passport.17k.com/ck/user/login'

data = {
    'loginName': '17346570232',
    'password': 'xlg17346570232'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'Cookie': 'GUID=a019343a-f892-44a3-8cc5-58977a497d50; c_channel=0; c_csc=web; acw_tc=276082a517130097186356061ea50fedb325b09e7e5811e4c5cd30b8c06eab; acw_sc__v2=661a743609ecae3e570d651986c9a5e6f2fa8adb; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F98%252F90%252F96139098.jpg-88x88%253Fv%253D1650527904000%26id%3D96139098%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BqYx51ZhI1%26e%3D1728561749%26s%3D290e10d1a5e07755; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2296139098%22%2C%22%24device_id%22%3A%2218ecd60b5dc74e-0dd0d9ab62dea6-4c657b58-2073600-18ecd60b5ddf28%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22a019343a-f892-44a3-8cc5-58977a497d50%22%7D',
}

res = requests.post(url, data=data, headers=headers)
print(res.text)
print(dict(res.cookies))
