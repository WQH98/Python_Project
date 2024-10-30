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

bingDetectionStop = False# os.getenv("bingDetectionStop")


# 获取用户信息
def getDashboard(bingCK):
    try:
        url = 'https://rewards.bing.com/pointsbreakdown'
        headers = {
            "cookie": bingCK,
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"
        };
        resp = requests.get(url, headers=headers).text
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
        }
        resp = requests.get(url, headers=headers).text
        str_start = 'RewardsBalance":'
        str_end = ',"GiveBalance'
        retStr = find(resp, str_start, str_end)
        return retStr
    except Exception as e:
        return '调用接口出现异常' + str(e)


# 搜索
def bing_rewards(q_str, bingCK, isPc):
    try:
        url = f'https://cn.bing.com/search?q={q_str}&qs=n&form=QBRE&=%25eManage%20Your%20Search%20History%25E&sp=-1&lq=0&pq=1&sc=10-1&sk=&cvid=18AEE186FE5E43888DFB3B69CB8C4770&ghsh=0&ghacc=0&ghpl=&sid=20DD92B87C2E63312D4281737D2F6223&format=snrjson&jsoncbid=7'
        if isPc == 1:
            ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
        else:
            ua = "Mozilla/5.0 (Linux; Android 12; Mi 10 Pro Build/SKQ1.220303.001; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 BingSapphire/23.5.2110003534"

        headers = {
            "cookie": bingCK,
            "referer": "https://rewards.bing.com/",
            "User-Agent": ua
        }
        resp = requests.get(url, headers=headers)
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
            new_Balance = getBalance(bingCK)
            printLog(f'积分', new_Balance)
            if bingDetectionStop != 'false':
                if getBalanceGap(old_Balance, new_Balance) <= 0:
                    printLog('检测', '积分未变动，停止运行！')
                    break
                old_Balance = new_Balance
            rand = random.randint(3, 5)
            time.sleep(rand)
    else:
        # pc端搜索35次
        for i in range(35):
            q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
            printLog(f'电脑搜索第{i + 1}次', bing_rewards(q_str, bingCK, 1))
            new_Balance = getBalance(bingCK)
            printLog(f'积分', new_Balance)
            if bingDetectionStop != 'false':
                if getBalanceGap(old_Balance, new_Balance) <= 0:
                    printLog('检测', '积分未变动，停止运行！')
                    break
                old_Balance = new_Balance
            rand = random.randint(3, 5)
            time.sleep(rand)
            # 安卓端搜索20次
        for i in range(20):
            q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
            printLog(f'安卓搜索第{i + 1}次', bing_rewards(q_str, bingCK, 0))
            new_Balance = getBalance(bingCK)
            printLog(f'积分', new_Balance)
            if bingDetectionStop != 'false':
                if getBalanceGap(old_Balance, new_Balance) <= 0:
                    printLog('检测', '积分未变动，停止运行！')
                    break
                old_Balance = new_Balance
            rand = random.randint(3, 5)
            time.sleep(rand)
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
    bingCK = os.getenv("bingCK")
    # bingCK = "MUID=3067D34D4F626B023505C0ED4E996AEE; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=366A3821406D4877BFBB253A14E3DF05&dmnchg=1; ANON=A=52551A6B753C52BCDDDBD4D3FFFFFFFF; MUIDB=3067D34D4F626B023505C0ED4E996AEE; MUIDV=NU=1; SnrOvr=X=rebateson; MSCC=cid=zbu0syhvyutcxak7dnd6pjw7-c1=2-c2=2-c3=2; MMCASM=ID=FC780CAC0D8342EF85E741FC3735665B; ANIMIA=FRE=1; _tarLang=default=zh-Hans; _TTSS_IN=hist=WyJlbiIsImF1dG8tZGV0ZWN0Il0=&isADRU=0; _TTSS_OUT=hist=WyJ6aC1IYW5zIl0=; WLS=C=00829e7a37c416a0&N=%e5%ba%86%e6%b5%a9; SRCHS=PC=CNNDDB; _Rwho=u=d; _EDGE_S=SID=20DD92B87C2E63312D4281737D2F6223&mkt=zh-cn; _clck=16vpx95|2|fgr|1|1373; _uetsid=bb0ac9e0845911eea42475949c12ccd2; _uetvid=b3121760635f11ee8acfd1d70e73094a; _U=1oShBBAFodG6JxYv6m5Y31Z0bWXStR6H09NGz1lnhUc8s469LJVwOKr4q9nDw2d73x-db4UXKnhCASG6bkKvjZSzPjsCOZQwyDcKo9XByEuHAlcmVYWR1NPTHxIuoK6UIxoTXlgZ2L04EnD1YQa9VfBESGa8ZmPcrFT8WzvCNOxSUB6s5gueDXS8KP1wZ8UsrtRhqXK_Xlev1zWwiepqI4fMMYNj3PhwoxR2d1RTKH_k; SRCHUSR=DOB=20231004&T=1700126885000; _UR=QS=0&TQS=0; ipv6=hit=1700130568235&t=4; MicrosoftApplicationsTelemetryDeviceId=abaa3684-251c-4ef8-8a4e-4bfea9e4d6e0; SNRHOP=I=&TS=; ENSEARCH=BENVER=1; _HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0xMS0xNlQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6NywiVG9iYnMiOjB9; ai_session=LpswEFQNVGaAuGuCH2uJ7v|1700126970067|1700127826215; USRLOC=HS=1&ELOC=LAT=34.56636428833008|LON=105.69285583496094|N=Qinzhou%20District%2C%20Gansu|ELT=2|&CLOC=LAT=34.566365901692265|LON=105.69285475450292|A=733.4464586120832|TS=231116001219|SRC=W; _FP=hta=on; GC=4O8D_I4WsF5faw23a-YCWFY3wJjguorkLrBpXko5dRf8G4aMyDwMpgYNkXLopB-txRKjopjvojtYIeF9UZnISw; _clsk=80oxlp|1700127888176|39|0|r.clarity.ms/collect; SRCHHPGUSR=SRCHLANG=en&DM=1&THEME=1&HV=1700127920&CW=859&CH=932&SCW=1164&SCH=2252&BRW=NOTP&BRH=M&DPR=1.0&UTC=480&PV=10.0.0&BZA=0&PRVCW=859&PRVCH=932&EXLTT=31&WEBTHEME=2&PR=1&IG=3F5F1AFA2CF44440A7EAD2320F0C485A;"
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
