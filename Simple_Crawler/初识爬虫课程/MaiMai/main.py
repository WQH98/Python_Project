import requests
import json

url = "https://maimai.cn/sdk/web/content/get_list"

headers = {
    "cookie": "seid=s1694833088062; guid=GBoaGxAYHxoQGx4aExAYGxofEE4TGRMQTBlLGRBJT08aEE9JTB1WGx8dGBMdHB9WGxIEEhkTGwQaBBwbGwVNTm8KHBkEHRkfBUNYS0xLeQoaBBoEGgQcGxsFT0dFWEJpCgNFQUlPbQpPQUNGCgZmZ35iYQIKHBkEHRkfBV5DYUhPfU9GWlprCgMeHFIKER4cREN9ChEaBBobCn5kClldRU5EQ30CChoEHwVLRkZDUEVn; csrftoken=TOn3np38-ppphJZSEqFNaaSxojyOle8fuau8; AGL_USER_ID=80b0c23f-05db-4528-86e9-412fa70cba37; _buuid=05c83745-c584-457d-aea8-08fd73cdb23b; browser_fingerprint=9A3F25BF; gdxidpyhxdE=7VRfXX6S8aCaD1ChWaRALqEH%2FUpU%2BJ8mJv59rqXEc%2Bs2e19%2Fhp7X8RAy%5CugzG%5CLgw7lBrrBzImyukwKvXlJgdbQt9TxYhmgxsADlEDpWbZ6Evd7Lk5Vr4UU5hGm%5CbAYyZlBOQQQewTEKXGhU2chKofTz7JTEq9zZ6zILV72Z%2F%5CPNKg3S%3A1694834006643; YD00198168557789%3AWM_NI=9qjVc5zqj6Trm0nsix35GLkmDpcY0QSNFPGpmwUPiKjnrErciJ4J7n65HkKgDY4gr%2FtTs9saWtq%2FOVCu%2Bbb83k9ecb80fmiR%2FAoWjjPRvgk7vKMMShP4jTBGOX3wljpWekg%3D; YD00198168557789%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea8e9469af5a4aef86488868ba3d85f868e9e86d5638a91ab92e85db4aef791d52af0fea7c3b92afbafa6b7e23fbaafa6d7d77aaff0a294ec74f1eb89adea6788b0adbab35b91928ab1c67cafa99bb1ec41aab2bea6f169ab96fcabb666f6eb888cca6d8887fc88f125b88cbddaf26b95acbfd0ce5e81abe583e134f1b5f786e26afcf0aa8eec5aed9fa1b8e962948eba88ea3db69583aed26494eca6b5c14d8d88fd98ef62b489ab8ce637e2a3; YD00198168557789%3AWM_TID=Ia3%2BkEEfdL1BQUVEFQPVjIaa6OW4694E; u=240063956; u.sig=5etwvJc-FJN3_DkyytumU2qeVEM; access_token=1.3e2d3e71e57eeb0d0b80fce3c3693b1e; access_token.sig=uukiLNtgUyZmPsPzc6gWAiDBHlk; u=240063956; u.sig=5etwvJc-FJN3_DkyytumU2qeVEM; access_token=1.3e2d3e71e57eeb0d0b80fce3c3693b1e; access_token.sig=uukiLNtgUyZmPsPzc6gWAiDBHlk; channel=www; channel.sig=tNJvAmArXf-qy3NgrB7afdGlanM; maimai_version=4.0.0; maimai_version.sig=kbniK4IntVXmJq6Vmvk3iHsSv-Y; session=eyJzZWNyZXQiOiJWTHQ4MWs0VEJhN1ZrWnNBMzJlZk4tSzgiLCJ1IjoiMjQwMDYzOTU2IiwiX2V4cGlyZSI6MTY5NDkxOTY0NjM4MywiX21heEFnZSI6ODY0MDAwMDB9; session.sig=CX2zD0VEnxIrNA_OjkbWfEIv0Zc",
    "X-Csrf-Token": "TOn3np38-ppphJZSEqFNaaSxojyOle8fuau8"
}


def craw_page(page_number):
    params = {
        "api": "gossip/v3/square",
        "u": "240063956",
        "page": page_number,
        "before_id": 0,
    }

    resp = requests.get(url, params=params, headers=headers)
    # print(resp.status_code)
    data = json.loads(resp.text)
    datas = []
    for text in data["list"]:
        datas.append(text["text"])

    return datas


with open("result of maimai.txt", "w+", encoding="utf-8") as f:
    for page in range(1, 11):
        print("craw page", page)

        datas = craw_page(page)
        f.write("\n".join(datas) + "\n")
