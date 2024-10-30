"""
Edge必应自动搜索赚积分
使用Edge浏览器打开必应 https://rewards.bing.com/ F12抓取Cookie即可  正确的CK格式是以MUID=xxxxxxx开头的
当前版本：v1.4

变量名：bingCK  多账号换行
bingDetectionStop 是否检测到积分未增长自动停止任务  默认为true  不需要该功能则额外定义变量，值为false

如果执行的发现积分不增长，且脚本上显示的积分跟实际不符，很有可能不是同一个账号的cookie，建议重新抓取。
玄学报错目前无解，凑合用吧！
"""
import requests
import os
import time
import random
import json
import datetime
import re
import urllib.parse
from time import strftime

old_Balance = 0
bingDetectionStop = os.getenv("bingDetectionStop")

proxies = {
    "http": "",
    "https": ""
}


# 获取用户信息
def getDashboard(bingCK):
    try:
        url = 'https://rewards.bing.com/pointsbreakdown'
        headers = {
            "cookie": bingCK,
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"
        };

        resp = requests.get(url, headers=headers, proxies=proxies).text
        str_start = 'var dashboard = '
        str_end = '{}};'
        retStr = find(resp, str_start, str_end) + "{}}"
        return retStr
    except Exception as e:
        return '调用接口出现异常' + str(e)


# 获取当前积分
def getBalance(bingCK):
    try:
        url = 'https://cn.bing.com/rewardsapp/reportActivity'
        headers = {
            "cookie": bingCK,
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"
        };
        # print(proxies["http"], proxies["https"])
        resp = requests.get(url, headers=headers, proxies=proxies).text
        str_start = 'RewardsBalance":'
        str_end = ',"GiveBalance'
        retStr = find(resp, str_start, str_end)
        return retStr
    except Exception as e:
        return '调用接口出现异常' + str(e)


# 搜索
def bing_rewards(q_str, bingCK, isPc):
    try:
        url = f'https://cn.bing.com/search?q={q_str}&qs=n&form=QBRE&pc=CNNDDB&sp=-1&lq=0&pq={q_str}&sc=0-13&sk=&cvid=8C46527A5AB84D8894D0F8C68ED04494ghsh=0&ghacc=0&ghpl='

        if isPc == 1:
            url = f'https://cn.bing.com/search?q={q_str}&qs=n&form=QBRE&pc=CNNDDB&sp=-1&lq=0&pq={q_str}&sc=0-13&sk=&cvid=8C46527A5AB84D8894D0F8C68ED04494ghsh=0&ghacc=0&ghpl='
            ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0"
        else:
            url = f"https://cn.bing.com/search?q={q_str}&setmkt=zh-CN&PC=EMMX01&form=L2MT2E&scope=web"
            ua = "Mozilla/5.0 (Linux; Android 12; Mi 10 Pro Build/SKQ1.220303.001; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 BingSapphire/23.5.2110003534"

        headers = {
            "cookie": bingCK,
            "referer": "https://cn.bing.com",
            "User-Agent": ua
        }
        resp = requests.get(url, headers=headers, proxies=proxies)
        code = resp.status_code
        if code == 200:
            msg = '成功'
        else:
            msg = '失败'
        retStr = msg
        return retStr
    except Exception as e:
        return '调用接口出现异常' + str(e)


# 随机生成一个汉字
def get_random_char():
    # 汉字编码的范围是0x4e00 ~ 0x9fa5
    random.seed()
    val = random.randint(0x4e00, 0x9fa5)
    # 转换为Unicode编码
    return chr(val)


# 分割函数
def find(str, str_start, str_end):
    start_index = str.find(str_start) + len(str_start)
    end_index = str.find(str_end)
    retStr = str[start_index: end_index].rstrip()
    return retStr


# 执行
def startMain(bingCK):
    '''
    try:
        userDashboard_json = json.loads(getDashboard(bingCK))
        activeLevel = userDashboard_json['userStatus']['levelInfo']['activeLevel']
        activeLevelName = userDashboard_json['userStatus']['levelInfo']['activeLevelName']
        progress = userDashboard_json['userStatus']['levelInfo']['progress']
        progressMax = userDashboard_json['userStatus']['levelInfo']['progressMax']
        if activeLevel == 'Level1':
            printLog('当前等级',f'{activeLevelName}[{progress}/{progressMax}]')
        else:
            printLog('当前等级',f'{activeLevelName}[{progress}]')
    except Exception as e:
        activeLevel = 'Level2'
        printLog('当前等级','获取失败')
    '''
    # 根据当前积分判断用户组
    start_Balance = getBalance(bingCK)
    if int(start_Balance) < 500:
        activeLevel = 'Level1'
        printLog('当前用户组', '第一阶段')
        upBalance = getBalanceGap(start_Balance, 500)
        printLog('距离升级下一阶段', f'还需要{upBalance}积分')
    else:
        activeLevel = 'Level2'
        printLog('当前用户组', '第二阶段')
    old_Balance = start_Balance
    if activeLevel == 'Level1':
        # pc端搜索10次
        for i in range(10):
            q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
            printLog(f'电脑搜索第{i + 1}次', bing_rewards(q_str, bingCK, 1))
            rand = random.randint(4, 5)
            time.sleep(rand)
            new_Balance = getBalance(bingCK)
            printLog(f'积分', new_Balance)
            if bingDetectionStop != 'false':
                if getBalanceGap(old_Balance, new_Balance) <= 0:
                    printLog('检测', '积分未变动，停止运行！')
                    break
                old_Balance = new_Balance
    else:
        # pc端搜索35次
        for i in range(35):
            q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
            printLog(f'电脑搜索第{i + 1}次', bing_rewards(q_str, bingCK, 1))
            rand = random.randint(4, 5)
            time.sleep(rand)
            new_Balance = getBalance(bingCK)
            printLog(f'积分', new_Balance)
            if bingDetectionStop != 'false':
                if getBalanceGap(old_Balance, new_Balance) <= 0:
                    printLog('检测', '积分未变动，停止运行！')
                    break
                old_Balance = new_Balance
            # 安卓端搜索20次
        for i in range(20):
            q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
            printLog(f'安卓搜索第{i + 1}次', bing_rewards(q_str, bingCK, 0))
            rand = random.randint(4, 5)
            time.sleep(rand)
            new_Balance = getBalance(bingCK)
            printLog(f'积分', new_Balance)
            if bingDetectionStop != 'false':
                if getBalanceGap(old_Balance, new_Balance) <= 0:
                    printLog('检测', '积分未变动，停止运行！')
                    break
                old_Balance = new_Balance

    end_Balance = getBalance(bingCK)
    increase_Balance = getBalanceGap(start_Balance, end_Balance)
    printLog('本次增加积分', f'{increase_Balance}')


# 计算积分增长数
def getBalanceGap(old_Balance, new_Balance):
    return int(new_Balance) - int(old_Balance)


# nvl函数
def nvl(str):
    if not str is None:
        out = str
    else:
        out = ''
    return out


# 输出日志
def printLog(title, msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now + f' [{title}]:' + nvl(msg))


if __name__ == '__main__':
    if bingDetectionStop == '':
        bingDetectionStop = 'true'
    url = "https://service.ipzan.com/core-extract?num=1&no=20230930146331307287&minute=3&format=json&protocol=1&pool=quality&secret=daogee708nejt4g"
    r = requests.get(url)
    r = json.loads(r.text)
    proxies["http"] = f'{r["data"]["list"][0]["ip"]}:{r["data"]["list"][0]["port"]}'
    proxies["https"] = f'{r["data"]["list"][0]["ip"]}:{r["data"]["list"][0]["port"]}'
    print(proxies["http"], proxies["https"])
    # bingCK = "MUID=245E56D9FE1D60E101DC42CCFF6161BA; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=7C5B10AF77A34837AEEA49823FD9D42F&dmnchg=1; ANON=A=52551A6B753C52BCDDDBD4D3FFFFFFFF; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; MUIDV=NU=1; MSPTC=0Zh5K83dB5qa1IPPVjjVQ2HEqwHRa6514CRYprwFfkM; SnrOvr=X=rebateson; MMCASM=ID=97B1F0A24A124B1F93E6879994BDB100; ANIMIA=FRE=1; MSCC=cid=mtafqyq8rwmj6woos8t16wsy-c1=2-c2=2-c3=2; MSCCSC=1; EDGSRCHHPGUSR=CIBV=1.1655.1; _clck=1g53ira%7C2%7Cfkm%7C1%7C1489; _EDGE_S=SID=3EEC5AF360EE660B2DE04EA561A46700; WLS=C=00829e7a37c416a0&N=%e5%ba%86%e6%b5%a9; SRCHS=PC=CNNDDB; USRLOC=HS=1&ELOC=LAT=34.57357406616211|LON=105.69229125976562|N=%E7%A7%A6%E5%B7%9E%E5%8C%BA%EF%BC%8C%E7%94%98%E8%82%83%E7%9C%81|ELT=2|&CLOC=LAT=34.574992519220686|LON=105.69330240969846|A=733.4464586120832|TS=240403070558|SRC=W&BID=MjQwNDAzMTUwNTU3X2I1ZDg5MDQ2ZjFlYTQ0M2ViOTgwMDdlMDkxY2E0YmU2MTdmNTEwYjZmNWMyNDBlNGRjODEzMmViMmIxYTViNzU=; _Rwho=u=d&ts=2024-04-03; dsc=order=BingPages; _U=11V2UtoiLrmwdHjSW5ViVX1YQj9ZsQPiAYRdPgLuJnx2dV31n2SMDpTedj633n6ZkVWLhlhJdfUZfZv1jlmIcZbxyTbcSaywW5Z_CRF9cOeSC2ZFhEDCYEYcj6VIkcky3JwBhTezYUWt3rIdxpaDqO-3XWh8MS6wA_SRhL6R_xTAMSyMB5QijBFCWb_OaLtx4DSJC9f-6eA38MMkE4SQND2QYcF0N1o2YqEpATGVwPq0; _uetsid=1179e8e0f15311ee8854f728cf9d8af5; _uetvid=73b77110be7511ee8c9783dd393862f3; _C_ETH=1; GC=lptsJ1pGEHUuZiqHH-K6gnSYfyQu-cXDXpfHFEnSU6WYKs545adR3cPtMhMBjsNVBpjRrxajAQR-h5XP1aU4Zw; _clsk=pjrg83%7C1712127898326%7C5%7C0%7Cb.clarity.ms%2Fcollect; SNRHOP=I=&TS=; SRCHUSR=DOB=20240129&T=1712128132000&POEX=W; ipv6=hit=1712131734996; _UR=QS=0&TQS=0; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wNC0wM1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoxLCJUb2JuIjowfQ==; _RwBf=r=1&ilt=0&ihpd=0&ispd=0&rc=12771&rb=12771&gb=0&rg=35830&pc=12662&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=1&l=2024-04-03T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-04-02T23:53:58.3482049-07:00&o=16&p=BINGTRIAL5TO250P201808&c=MY00IA&t=4759&s=2023-01-13T09:37:59.7422461+00:00&ts=2024-04-03T07:08:55.4298519+00:00&rwred=0&wls=0&wlb=0&wle=0&ccp=0&lka=0&lkt=0&aad=0&TH=&mta=0&e=cH_hqXk6Ob-rxu8ULeNcECLJxqLekA_08yviimXYBWDAGJZKukNQplKaqfZKYStbBPVXmGTrHfrBAs2DZYC-LQ&A=&rwflt=2024-03-28T02:37:02.2187588-07:00; _SS=SID=3EEC5AF360EE660B2DE04EA561A46700&PC=CNNDDB&R=12771&RB=12771&GB=0&RG=35830&RP=12662; SRCHHPGUSR=SRCHLANG=zh-Hans&DM=1&PV=10.0.0&BZA=0&HV=1712128212&BRW=NOTP&BRH=M&CW=817&CH=932&SCW=802&SCH=932&DPR=1.0&UTC=480&EXLTT=31&PRVCW=1912&PRVCH=932&IG=8EE35A8F70CD4CD38F07C5AC933CB322&THEME=1&PR=1&cdxupdttm=638450858501228047&CIBV=1.1633.0"
    bingCK = "MUID=245E56D9FE1D60E101DC42CCFF6161BA; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=7C5B10AF77A34837AEEA49823FD9D42F&dmnchg=1; ANON=A=52551A6B753C52BCDDDBD4D3FFFFFFFF; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; MUIDV=NU=1; MSPTC=0Zh5K83dB5qa1IPPVjjVQ2HEqwHRa6514CRYprwFfkM; MMCASM=ID=97B1F0A24A124B1F93E6879994BDB100; ANIMIA=FRE=1; MSCCSC=1; BFBUSR=CMUID=245E56D9FE1D60E101DC42CCFF6161BA; MicrosoftApplicationsTelemetryDeviceId=bd95cd5f-5a4c-439e-a188-ef3ec9ff69ff; mapc=rm=1; SnrOvr=X=rebateson; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; _UR=QS=0&TQS=0&cdxcls=0; EDGSRCHHPGUSR=CIBV=1.1759.0; MSCC=cid=eurd46gtpkn8n70iyxwibnzd-c1=2-c2=2-c3=2; _tarLang=default=zh-Hans&newFeature=tonetranslation; _TTSS_IN=hist=WyJjeSIsInpoLUhhbnMiLCJlbiIsImF1dG8tZGV0ZWN0Il0=&isADRU=0; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnMiXQ==; _uetvid=73b77110be7511ee8c9783dd393862f3; _EDGE_S=SID=0F417946D94E65D12C126DE4D89C64BD; WLS=C=00829e7a37c416a0&N=%e5%ba%86%e6%b5%a9; _U=1LQ-wzXXcXoCxPZQT6WYutHZ-gmQnfjCVOW27ePyPhwnEEZBYZrOuodcsjk0JDV5xDPPA93IWH2DJ7JXeSzex86CbSM_7GQ-2iMbYVH0JAzw1fk9uk1i1Jf0e8khWBlN5iEw3BpeSU8ry5Xv-mHP5FYXPq45WW4VCJoiszkj8aWZvHBz3frMjjF-I8-uHP8mzbh20alWvmWRmo9z7T7px5rWGmREnpld93qvDllocpYE; _clck=1g53ira%7C2%7Cfmq%7C1%7C1489; _clsk=143mm2c%7C1718669919212%7C2%7C1%7Cw.clarity.ms%2Fcollect; SRCHS=PC=CNNDDB; USRLOC=HS=1&ELOC=LAT=34.56698989868164|LON=105.69557189941406|N=%E7%A7%A6%E5%B7%9E%E5%8C%BA%EF%BC%8C%E7%94%98%E8%82%83%E7%9C%81|ELT=2|&CLOC=LAT=34.566989368119096|LON=105.69556928412115|A=733.4464586120832|TS=240618000603|SRC=W&BID=MjQwNjE4MDgwNjAzX2I1ZDg5MDQ2ZjFlYTQ0M2ViOTgwMDdlMDkxY2E0YmU2MTdmNTEwYjZmNWMyNDBlNGRjODEzMmViMmIxYTViNzU=; SRCHUSR=DOB=20240129&T=1718669999000&POEX=W; SNRHOP=I=&TS=; _Rwho=u=d&ts=2024-06-18; _HPVN=CS=eyJQbiI6eyJDbiI6MTIsIlN0IjowLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjEyLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjoxMiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wNi0xOFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjo2NCwiVG9ibiI6MH0=; ai_session=hNGAt9cGZw3soBIP6WFmfH|1718670003819|1718670003819; _SS=SID=0F417946D94E65D12C126DE4D89C64BD&PC=CNNDDB&R=8019&RB=8019&GB=0&RG=17915&RP=8019; GC=lptsJ1pGEHUuZiqHH-K6gnSYfyQu-cXDXpfHFEnSU6WbnKUaqiwjsZDnzjIycvK3ep6US3WuEuyokPpT4MncOw; _RwBf=r=1&ilt=0&ihpd=0&ispd=0&rc=8019&rb=8019&gb=0&rg=17915&pc=8019&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=21&l=2024-06-17T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-06-16T17:07:42.8223197-07:00&o=16&p=BINGTRIAL5TO250P201808&c=MY00IA&t=4759&s=2023-01-13T09:37:59.7422461+00:00&ts=2024-06-18T00:20:36.1277494+00:00&rwred=0&wls=0&wlb=0&wle=0&ccp=2&lka=0&lkt=0&aad=0&TH=&mta=0&e=cH_hqXk6Ob-rxu8ULeNcECLJxqLekA_08yviimXYBWDAGJZKukNQplKaqfZKYStbBPVXmGTrHfrBAs2DZYC-LQ&A=&rwflt=2024-06-17T08:27:43.9549240-07:00&cpt=0; ipv6=hit=1718673639844; SRCHHPGUSR=SRCHLANG=zh-Hans&DM=1&PV=10.0.0&BZA=0&HV=1718670038&BRW=NOTP&BRH=M&CW=402&CH=931&SCW=1164&SCH=2914&DPR=1.0&UTC=480&EXLTT=31&PRVCW=356&PRVCH=932&IG=7237D47E35C643C1BAEC651E00F7C5CA&THEME=1&PR=1&cdxupdttm=638450858501228047&CIBV=1.1732.0&OR=0&CMUID=245E56D9FE1D60E101DC42CCFF6161BA&WEBTHEME=1"
    cks = bingCK.split("\n")
    print(f"检测到{len(cks)}个账号,即将开始...")
    i = 1
    for ck in cks:
        print(f"\n---开始第{i}个账号---")
        i += 1
        startMain(ck)
        rand = random.randint(5, 20)
        if i > len(cks):
            break
        print(f"\n等待{rand}s后进行下一个账号")
        time.sleep(rand)
