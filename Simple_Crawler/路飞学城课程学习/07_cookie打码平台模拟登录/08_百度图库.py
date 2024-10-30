import os.path
import re
import requests
import json


def get_word():
    word = str(input("请输入您想搜索的关键字："))
    return word


def get_html(word):
    ret_urls = []
    url = 'https://image.baidu.com/search/acjson'
    params = {
        'tn': 'resultjson_com',
        'logid': '7912364142487242197',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'fr': '',
        'word': word,
        'queryWord': word,
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '0',
        'ic': '0',
        'hd': '0',
        'latest': '0',
        'copyright': '0',
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'expermode': '',
        'nojc': '',
        'isAsync': '',
        'pn': '30',
        'rn': '30',
        'gsm': '1e',
        '1712994297466': '',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
        'Cookie': 'BIDUPSID=9AD35D9A7248D943FFB159CBD2B5737A; PSTM=1709198710; BAIDUID=9AD35D9A7248D943FFB159CBD2B5737A:SL=0:NR=10:FG=1; H_WISE_SIDS_BFESS=40171_39662_40206_40212_40216_40079_40365_40305_40373_40369_40407_40416_40310_40467_40461_40471_40317; BAIDUID_BFESS=9AD35D9A7248D943FFB159CBD2B5737A:SL=0:NR=10:FG=1; ZFY=rL73QKxU6oImdN:ARqVQPiPuLyi5SwmUdcBUiNSS:BUfk:C; H_PS_PSSID=40171_40305_40373_40369_40416_39662_40511_40514_40397_60044_60024_60035_60048; H_WISE_SIDS=40171_40305_40373_40369_40416_39662_40511_40514_40397_60044_60024_60035_60048; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; userFrom=cn.bing.com; firstShowTip=1; indexPageSugList=%5B%22%E5%A3%81%E7%BA%B8%22%5D; cleanHistoryStatus=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; ab_sr=1.0.1_OThhOTE5YTg2MDEzNDgzNDcxY2JhMzZiMTM3ZTBmMDYzZGJiMjE2M2ZkYTY1OWRlYWNiMzdlNDU0MzJkYjFkMTljNDEzZmIxZTBlY2Y1YjUwY2FjMzAyZDkyZDBlMzBhMzhmMjMzMWU0Mjg1NTljNDU5YjliYTEzZDU2YjBkMWRhN2Y3YmQ0Mzg4MWFhMzY4ZWRkN2M1YjYxOWQ1OWFhYjk1ZGY1NWUxMjIzY2RlZjUzYTM3NGNjZjJmMmU0M2M2OGI5YWYwMmE3NWFhOGYxOTg0MWMwYzkyYjIzMmUxNGM=; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm',
        'Host': 'image.baidu.com',
        'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111110&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A3%81%E7%BA%B8'
    }

    res = requests.get(url, params=params, headers=headers).content.decode()
    js = json.loads(res)

    path = "./08_百度图库下载"
    if not os.path.exists(path):
        os.mkdir(path)
        print(f'未找到{path}文件夹 现在新建')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    }
    for i in range(0, 10):
        print(js['data'][i]['thumbURL'])
        print(js['data'][i]['fromPageTitle'])
        img_url = js['data'][i]['thumbURL']
        img_name = js['data'][i]['fromPageTitle']
        img_name = re.sub(r'[:/\\?*“”<>|]', '_', img_name)
        res = requests.get(img_url, headers=headers)
        with open(f'{path}/{i}_{img_name}.jpg', 'wb') as f:
            f.write(res.content)


if __name__ == '__main__':
    word = get_word()
    get_html(word)


