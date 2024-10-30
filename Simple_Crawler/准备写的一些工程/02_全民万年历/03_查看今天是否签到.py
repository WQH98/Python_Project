import requests
import time

now_time = str(int(time.time() * 1000))

url = 'https://hapi.qmrl888.com/v2/gcoin/checkInfo.api'

headers = {
    'Host': 'hapi.qmrl888.com',
    'deviceid': '3665258',
    'qmsign': 'nwp27IiAodZpUGeYjA1iKCiWScVIiF6lc0UP8EWiXiAXSDO1FuoP0ll/E8QJKfDC',
    'timestamp': now_time,
    'serverapi': '2',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; ONEPLUS A6000 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'osver': '11',
    'vercode': '53',
    'userid': '2200667',
    'usertoken': '4{qv>8mM4$gP}]@)[!}Bd2>R4qG~Y;H2r],YZ5*7F>_VLJZ6Y~b8JJ',
    'qm': '3BdJ3yCADB2r4e57',
    'os': 'Android',
    'app': 'oppo',
    'version': '4.6.4',
    'origin': 'https://he.qmrl888.com',
    'x-requested-with': 'com.aoyi.calendar',
}

resp = requests.get(url, headers=headers)
print(resp.text)
