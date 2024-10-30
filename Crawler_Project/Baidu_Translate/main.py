"""
百度翻译脚本 通过输入的单词 输出翻译结果
"""

import requests

url = "https://fanyi.baidu.com/sug"

kw = input("Please enter the word you want to query: ")

datas = {
    "kw": kw,
}

headers = {
    "content-length": str(len(datas)),
    # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    "X-Requested-With": "XMLHttpRequest",
}

r = requests.post(url, headers=headers, data=datas)

result = ""
for i in r.json()["data"]:
    result += i["v"] + '\n'
print(kw+":")
print(result)
