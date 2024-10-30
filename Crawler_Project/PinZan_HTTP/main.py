# 品赞HTTP签到 项目练习
import json
import requests

url = "https://service.ipzan.com/home/userWallet-receive"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43",
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZSI6IjE1NTg4NTQ3ODgwIiwic291cmNlIjoiaXB6YW4taG9tZS1vbmUiLCJ1c2VySWQiOiI2VlZVUEFGNTVHIiwiY2VydGlmeVN0YXR1cyI6MSwiaWF0IjoxNjk3NDE5ODc2LCJleHAiOjE2OTc2NzkwNzZ9.o8lEaH0oHZiud1L5Bva4B3K8_GARaCe5bngvteFr_sX_A_WoJeqY7j4BcUZKmGsQKCeUPkGwT5LFBSuuj28YcUj9XH6G9OL-Buuy702HqjkbprivcOhZT04WOsU7o-cD6mU10zn_jdACuqQk62WXjM6Q-yDIfUJ0ymQ8b3gH3kQ"
}

r = requests.get(url, headers=headers)
message = json.loads(r.text)
print(message['message'])
