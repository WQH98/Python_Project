import requests
import json
import os
import time
import random

delay = random.uniform(1, 2)
consecutive_skips = 0
visited_title_ids = set()
all_data = []
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ3ZW5ibyIsImF1ZCI6IndlbmJvbWluaSIsImlhdCI6MTcwMTA3NzE0OCwibmJmIjoxNzAxMDc3MTQ3LCJleHAiOjE3MDEwODA3NDgsImRhdGEiOnsidXNlcmlkIjoxNDg1MH19.ZHvB2djOMg8aKvf9H_8rDkLOieu7O_fo1VCg8X-_DXU"
sign = "dab352754f79462d70046e82a520a3e7ccf0007b"
accounts = os.getenv('wbdh')
uuids = accounts.split('\n')

num_of_accounts = len(uuids)
print(f"获取到 {num_of_accounts} 个账号")

for i, uuid in enumerate(uuids, start=1):
    try:
        print(f"正在处理第 {i} 个账号...")
        for j in range(1000):
            # 抽奖
            url = "https://wbdh.jiiimo.cn/api/prize/get"
            headers = {
                "Host": "wbdh.jiiimo.cn",
                "xweb_xhr": "1",
                "cookie": f"PHPSESSID=1aea29a12de2ec6ad3b28df5d78d1df7; expires=Tue, 28-Nov-2023 13:00:13 GMT; Max-Age=86400; path=/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309062b)XWEB/8461",
                "Token": token,
                "Accept": "*/*",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://servicewechat.com/wx0607abd12886662b/28/page-frame.html",
                "Accept-Language": "zh-CN,zh;q=0.9"
            }

            mids = [13, 14, 15, 16, 17, 18, 19, 20, 21]

            for mid in mids:
                data = {
                    "mid": str(mid),
                    "uuid": uuid,
                    "sign": sign
                }
                response = requests.post(url, headers=headers, data=data, verify=True)
                print(response.text)

                time.sleep(10)  # 添加10秒的时间间隔

            # 提现
            url = "https://wbdh.jiiimo.cn/api/user/tixian"
            headers = {
                "Host": "wbdh.jiiimo.cn",
                "xweb_xhr": "1",
                "cookie": f"PHPSESSID=1aea29a12de2ec6ad3b28df5d78d1df7; expires=Tue, 28-Nov-2023 14:46:30 GMT; Max-Age=86400; path=/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309062b)XWEB/8461",
                "Token": token,
                "Accept": "*/*",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://servicewechat.com/wx0607abd12886662b/28/page-frame.html",
                "Accept-Language": "zh-CN,zh;q=0.9"
            }
            data = {
                "uuid": uuid,
                "sign": sign
            }

            response = requests.post(url, headers=headers, data=data)
            print(response.json())

            time.sleep(10)  # 添加10秒的时间间隔

            break
    except Exception as e:
        print(f"处理第 {i} 个账号时出现异常：{str(e)}")
