import requests

url = "https://sh-gateway.shihuo.cn/v4/services/sh-goodsapi/app_swoole_shoe/preload/single"

params = {
    "devices": "ONEPLUS%20A6000",
    "gender": "2",
    "goods_id": "4721171",
    "sourceLocation": "oneRowOne%3A%5BN%5D",
    "tpExtra": "%7B%22sourceTp%22%3A%22home%3Asearch%3A%22%2C%22sourceTpName%22%3A%22%E8%B5%A4%E5%85%94%E4%B8%83pro%22%2C%22wsf%22%3A%22normal_search_words%22%2C%22ast%22%3A%22%E8%B5%A4%E5%85%94%E4%B8%83pro%22%2C%22is_inspire%22%3A0%2C%22dgReqId%22%3A%22SHSS_CG-POSTLQDALAPE_SPU_1%3AR1-L1-G12%7C%7CR1-L2-G23%7C%7CR1-L3-G35%22%2C%22si%22%3A%228001%22%2C%22skc%22%3A%22144753853%22%2C%22layer%22%3A%222%22%7D",
    "minVersion": "15670",
    "clientCode": "%7Bholder%7D",
    "v": "7.20.1",
    "channel": "huawei",
    "device": "ONEPLUS%20A6000",
    "platform": "android",
    "timestamp": "1710312582730",
}

headers = {
    "sh-token": "ev873aoeahM2RkMjgzMmQ5OWE4NDdmNDk02uaDcxmACoVeNwQ6LYIoiHOaw/B8RCSaIn5bmnUyFR1WpjWrVJWbcQBq6ESEZCUNakfTdLpZwum4DIqDFTIUkzjvBnias6o7ReMGAJj/9F9loyezFLKAd0mELQhzmedQqNN6lHWDk3ioqMwGuFCttw==",
    "user-agent": "Android 11 {T25lUGx1cw} CPU_ABI arm64-v8a CPU_ABI2  HARDWARE qcom MODEL {T05FUExVUyBBNjAwMA} network/WIFI shihuo/7.20.1 sc({holder},huawei) minVersion(15670) sh-dv-sign[v1|1d72c25f2451dbc4b411a64dea0cda530d2751f79b8da0aa]",
    # "acw_tc": "2f624a5117103327949058193e296220ac900e7aa44d003ec943426457f3cf",
    "sh-id": "s177hk03825e6d38128ddc198009eb04",
    "sh-sign": "E36059D60B756C7C4DC92AC11CA928A3",
    "shreqid": "E51F6A37E0C547F6D429757DF98A1E94",
    "sh_session": "6fd1d0f1dc1a44b0b9c82ea797abf62b_foreground_12464",
    "sk": "9Oo4F9ESdLzMBgj6VF1SZyq5GyZVyW4YdSD74Ksb3k8tjA9TxUCdw3GDI1csLRLlAsFsdPt1RzKOteZnsFfWqFFtzU1w",
    "appid": "app",
    "Host": "sh-gateway.shihuo.cn",
    "platform": "android",
    "timestamp": "1710334576530",
    "app-v": "7.20.1",
}

cookies = {
    "acw_tc": "2f624a5117103327949058193e296220ac900e7aa44d003ec943426457f3cf",
}

r = requests.get(url, params=params, headers=headers, cookies=cookies)

print(r.status_code)

data_list = r.json()
for data in data_list["data"]["info"]["styles"]["list"]:
    print(data["name"])
    for k, v in data["priceAll"].items():
        print("------", k, v)
