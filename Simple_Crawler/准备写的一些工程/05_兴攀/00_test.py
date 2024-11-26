import json

import requests

url = "https://p.xpfarm.cn/treemp/wx.Login/index"

headers = {
    "content-length": "1303",
    "xweb_xhr": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) UnifiedPCWindowsWechat(0xf254001a) XWEB/11503",
    "content-type": "application/json",
    "accept": "*/*",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://servicewechat.com/wx27e219ff3142b7c8/63/page-frame.html",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9"
}

data = {
    "cloudID": "86_U3eRpdwmEoXECACV6cSmyo59QVEi0AU57aGtZ9hQnZz_2MBmCOxyjnhT4kA",
    "encryptedData": "pdWHF0uN5XEi6LbQDvySw4ICNCYTjefF9NnP5Z9ZFT0GYtsWD/7pILksEZZfF8OMBJxGo7CeJrrQjeMalMC8cNPC+wePreYISZYhYgLIHxA5zbt5Ql2eQMSvMd82a9pmnYkwVfjbx49lxswDlLQvVlmJ/HVHDBoKKxlPx3g5THe/YpCzWeyxk1wOJwsTsdnTQc+sLBi/W/tEU3EekJetjBpV12QIWDQJUmy3CArsJ2UMYjhP+eOojvl1Nl65Yj1bmWfptCNrRICx9UsoP9GfpfhG7MlKbTNHR+SrpU6z8fKomJD/zFfKSphRj7LVoT3Qghi/gLWKliP5ZTEkDHEzPmOv8iFgEWc18cxBlz9d1QrWWHfwOrl/4KADruoovyYtjftCmCqP4KkvpIWqzelra7CEcrwwx/4WFjPszDHjU+mXYHZ+Ly1qqBaM8JaUyc0h",
    "iv": "bEZ+Hs81IrvjNZxika7ESQ==",
    "signature": "01b5b50dafa2d5255e3a0eb2bdeb70b9c57b5404",
    "userInfo": {
        "nickName": "微信用户",
        "gender": 0,
        "language": "",
        "city": "",
        "province": "",
        "country": "",
        "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132",
        "is_demote": "true"
    },
    "rawData": "{\"nickName\":\"微信用户\",\"gender\":0,\"language\":\"\",\"city\":\"\",\"province\":\"\",\"country\":\"\",\"avatarUrl\":\"https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132\",\"is_demote\":true}",
    "errMsg": "getUserProfile:ok",
    "openid": "o4WMG41rENEG3_YmaHSvJj0uJ-4g",
    "unionid": "oT4Cj0zhqmYouiyd5zpHn82jaDUY"
}

resp = requests.post(url, headers=headers, json=data, verify=False).json()
print(resp["data"]["token"])
