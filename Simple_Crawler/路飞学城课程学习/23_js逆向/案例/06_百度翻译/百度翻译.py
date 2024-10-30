# 如果js代码中含有中文 则引入以下代码
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import requests
import execjs

'''
    输入要查询的单词
'''
word = 'shit'

'''
    使用js文件获取sign
    读取js代码并运行 返回sign值
'''
f = open('./百度翻译破解sign.js', mode='r', encoding='utf-8')
js_code = f.read()
f.close()
js = execjs.compile(js_code)
sign = js.call('sign', word)


'''
    组装所需要的数据 头部
    发包
'''
url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

data = {
    'from': 'en',
    'to': 'zh',
    'query': word,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': sign,
    'token': 'ce883f88bdf5809fd7907a3af2112299',
    'domain': 'common',
    'ts': '1717579663109'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'Cookie': 'BIDUPSID=9AD35D9A7248D943FFB159CBD2B5737A; PSTM=1709198710; BAIDUID=9AD35D9A7248D943FFB159CBD2B5737A:SL=0:NR=10:FG=1; BAIDUID_BFESS=9AD35D9A7248D943FFB159CBD2B5737A:SL=0:NR=10:FG=1; H_WISE_SIDS=40171_40305_40373_40369_40416_39662_40511_40514_40397_60044_60024_60035_60048; BAIDU_WISE_UID=wapp_1713013814883_487; BDUSS=xIWjRQT2ZmYU01NmJYRzR4SFM4TlJ0dE1QcE0xVkZGRU85QWNhWVd-eHJ3RVptRUFBQUFBJCQAAAAAAAAAAAEAAABxFsldtqvJ2ezhufrp5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGszH2ZrMx9mTm; BDUSS_BFESS=xIWjRQT2ZmYU01NmJYRzR4SFM4TlJ0dE1QcE0xVkZGRU85QWNhWVd-eHJ3RVptRUFBQUFBJCQAAAAAAAAAAAEAAABxFsldtqvJ2ezhufrp5AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGszH2ZrMx9mTm; H_WISE_SIDS_BFESS=40171_40305_40373_40369_40416_39662_40511_40514_40397_60044_60024_60035_60048; ZFY=AItaqHVfsFbx6Tn:BZLj:AaZPZ6UU7FBnJbgK4XP9DDJs:C; H_PS_PSSID=60270_60278_60289_60297_60253; __bid_n=18fdd013c440576541377a; smallFlowVersion=old; RT="z=1&dm=baidu.com&si=b3898ddc-ae6a-4cf7-92c3-10059ccfa810&ss=lx18ksoa&sl=b&tt=wv2&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=eqyf&ul=fmxi&hd=fn4i"; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1717556869; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1717556869; APPGUIDE_10_7_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1',
    'Referer': 'https://fanyi.baidu.com/',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
}

resp = requests.post(url=url, headers=headers, data=data)

print(resp.json())
