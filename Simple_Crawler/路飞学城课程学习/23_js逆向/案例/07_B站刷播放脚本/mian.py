import requests
import re
import json


def get_cookies1(session):
    # 拿到cookies buvid3 b_nut
    url = 'https://www.bilibili.com/video/BV1Hi421Y79v/?spm_id_from=333.337.search-card.all.click'
    resp = session.get(url)
    tmp = re.findall(r'__INITIAL_STATE__=(.*?);\(function', resp.text)
    tmp = json.loads(tmp[0])
    aid = tmp['aid']
    cid = tmp['videoData']['cid']
    session.cookies['CURRENT_FNVAL'] = '4048'
    session.cookies['buvid4'] = 'CF99AF7E-352E-8340-DA8B-881F60A2E28250956-024071600-P6Lc8aukfDTh2FBZMi4Hsg%3D%3D'
    url = 'https://api.bilibili.com/x/player/v2'
    params = {
        'aid': aid,
        'cid': cid,
    }
    resp = session.get(url)
    print(resp.text)
    return aid, cid


if __name__ == '__main__':
    session = requests.session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    aid, cid = get_cookies1(session)
    print(session.cookies)
