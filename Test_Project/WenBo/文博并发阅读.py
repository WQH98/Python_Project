"""
uuid换行隔开
"""
import requests
import json
import os
import time
import sys
import random
from concurrent.futures import ThreadPoolExecutor

delay = random.uniform(1, 1)
consecutive_skips = 0
visited_title_ids = set()
all_data = []
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ3ZW5ibyIsImF1ZCI6IndlbmJvbWluaSIsImlhdCI6MTcwMTA4MTg1NywibmJmIjoxNzAxMDgxODU2LCJleHAiOjE3MDEwODU0NTcsImRhdGEiOnsidXNlcmlkIjoyMDQxMH19.xcV78u6YBBzYD8R-nppL4RRyY4KF6K6geGBYgE_jg6E"
sign = "c304cc000edce4f7f1d07f32ebfddcb7126dfbbd"
# accounts = os.getenv('wbdh')
accounts = "52144b8f9ed8759940fcd83732789b5d"
uuids = accounts.split('\n')

# uuids = "52144b8f9ed8759940fcd83732789b5d"

num_of_accounts = len(uuids)
print(f"获取到 {num_of_accounts} 个账号")

def process_account(uuid):
    midnum = 12
    for j in range(1000):
        url = "https://wbdh.jiiimo.cn/api/question/get"
        headers = {
            "Host": "wbdh.jiiimo.cn",
            "Connection": "keep-alive",
            "Content-Length": "83",
            "charset": "utf-8",
            "cookie": "PHPSESSID=70376958b92df2e75a9795b8ba24b5cb; expires=Thu, 23-Nov-2023 17:19:38 GMT; Max-Age=86400; path=/",
            "User-Agent": "Mozilla/5.0 (Linux; Android 14; 2211133C Build/UKQ1.230705.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 XWEB/1110017 MMWEBSDK/20230805 MMWEBID/525 MicroMessenger/8.0.42.2460(0x28002A35) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip,compress,br,deflate",
            "token": token,
            "Referer": "https://servicewechat.com/wx0607abd12886662b/23/page-frame.html"
        }
        data = f"mid={midnum}&qid=&uuid={uuid}&sign='{sign}'"
        response = requests.post(url, headers=headers, data=data).json()

        if response['code'] == 1:
            print(response['msg'])
            break

        number = response['data']['number']
        print(f"【{midnum}】\n【题目】: {response['data']['title']}\n【选项】: {response['data']['options']}")
        aid = response['data']['id']

        with open('3.json', 'r', encoding='utf-8') as json_file:
            json_content = json.load(json_file)

        matching_question = next((question for question in json_content if question["title_id"] == aid), "A")

        if matching_question != "A":
            options = matching_question["options"]
            print(f"第{number}题的选项：{options}")
        else:
            print(f"此题不在题库，准备收纳")
            options = "A"

        url1 = "https://wbdh.jiiimo.cn/api/question/post"
        data1 = f"id={aid}&select={options}&wyy=0&wyy_point=0&uuid={uuid}&sign={sign}"
        time.sleep(delay)
        response1 = requests.post(url1, headers=headers, data=data1).json()
        print(response1)

        if response1['code'] == 1 and response1['msg'] == '答题超过每日上限，请明天再来答题':
            print(response1['msg'])
            break

        if response1['code'] == 1 and response1['msg'] == '请稍后再试':
            print(response1['msg'])
            time.sleep(60)
            continue

        print(f"【答案】{response1['data']['answer']}\n")
        optionsk = list(response1['data']['answer'].keys())
        optionskey = optionsk[0]
        titleid = response['data']['id']

        if number == 12:
            print(f"第{midnum}轮已答完")
            time.sleep(delay)
            midnum += 1
            if midnum == 22:
                midnum = 12



        title = response['data']['title']
        visited_title_ids.add(titleid)

        current_data = {
            'title': title,
            'title_id': titleid,
            'options': optionskey,
        }

        all_data.append(current_data)
        time.sleep(2)

        output_file_path = '3.json'
        if current_data not in json_content:
            json_content.append(current_data)
            with open('3.json', 'w', encoding='utf-8') as json_file:
                json.dump(json_content, json_file, ensure_ascii=False, indent=2)
            print(f'数据已追加到 3.json\n')


with ThreadPoolExecutor(max_workers=num_of_accounts) as executor:
    for uuid in uuids:
        executor.submit(process_account, uuid)
        time.sleep(1)
    time.sleep(20)
