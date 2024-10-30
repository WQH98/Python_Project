import requests

url = "https://sh-api.shihuo.cn/daga/search/goods/v1"

params = {
    "minVersion": "15670",
    "clientCode": "{holder}",
    "v": "7.20.1",
    "channel": "huawei",
    "device": "ONEPLUS A6000",
    "platform": "android",
    "timestamp": "1710311127564",
    "token": "d25ba600abb3c45f0ee16bcc7e7c147e"
}

datas = {
    "from": "home",
    "isHot": "false",
    "keywords": "赤兔七pro",
    "lspm": "d974c9b72d3de135",
    "needAttrs": 1,
    "page": "1",
    "pageContext": """{"pageId":"homeSearchList_023CE88484503EA1857AF3A84C7B33C3","ptiRoot":{"biz":"{\"layer\":\"1\"}","name":"","toInfo":{"route":"homeSearch","back_keywords":"防晒霜"},"id":"home:searchInput","pageId":"appHome_A0C0A1A168B0EBC6E2165065D6E9172B","pageOptions":{"haveSkin":"1"}},"layer":"3"}""",
    "pageSize": "20",
    "page_route": "homeSearchList",
    "predictSex": "2",
    "use_type": "2",
    "user_input": "%E8%B5%A4%E5%85%94%E4%B8%83pro"
}

r = requests.post(url, params=params, json=datas)

data_list = r.json()
for data in data_list["data"]["lists"]:
    print(data["name"])
    for ele in data["style_lists"]:
        print("------", ele["goods_id"], ele["name"], ele["price"])


