# 雨云签到练习
# 签到以后status是2
# 一天一次


import json
import requests

url = "https://api.v2.rainyun.com/user/reward/tasks"

headers = {
    "X-Api-Key": "62RhGCQ2yFOCLOh8quUPqcgLSETGKvb4",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43",
}

r = requests.get(url, headers=headers)
result = json.loads(r.text)
print("检查今日是否已经签到")
data = result["data"][0]
print(data["Status"])
if data["Status"] == 1:
    print("开始签到")
    r = requests.post(url, headers=headers, json={"task_name": "每日签到"})
    print(r.text)
    result = json.loads(r.text)
    print(result)
else:
    print("今日已签到")


