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


# 获取今日积分
def get_today_balance():
    try:
        now_time = str(int(time.time() * 1000))
        url = f'https://rewards.bing.com/api/getuserinfo?type=1&X-Requested-With=XMLHttpRequest&_={now_time}'

        headers = {
            'sec-ms-gec': 'AB016AA566E882EFB75C93251228E64ACC8D528E2C5BD9CC2EA1E3939ADCC542',
            'x-client-data': 'eyIxIjoiMCIsIjEwIjoiXCJYM0E0STRtRjk3a0RhbVdLenhDeTJBV2Q1bjVtVFd6V3RTK29LaXhocHNBPVwiIiwiMiI6IjAiLCIzIjoiMCIsIjQiOiI3OTcyOTE1NDY5NTIzNTQ5MTE0IiwiNSI6IlwicWYwdDFFL1lIcUcxQmVXSjhaK1BDaTZydkNCMXFoTXRYUVJxWUR2Ti9nND1cIiIsIjYiOiJzdGFibGUiLCI3IjoiMzk3NzEzOTcxNjA5OSIsIjkiOiJkZXNrdG9wIn0=',
            'referer': 'https://rewards.bing.com/',
            'sec-ms-gec-version': '1-127.0.2651.86',
            "cookie": "_C_Auth=; MUID=245E56D9FE1D60E101DC42CCFF6161BA; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=7C5B10AF77A34837AEEA49823FD9D42F&dmnchg=1; ANON=A=52551A6B753C52BCDDDBD4D3FFFFFFFF; MUIDV=NU=1; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; vdp=%7B%22ex%22%3Atrue%2C%22red%22%3Afalse%7D; MicrosoftApplicationsTelemetryDeviceId=a026a378-86fc-4413-b483-6deb695ace49; MicrosoftApplicationsTelemetryFirstLaunchTime=2024-01-29T07:10:15.039Z; MSPTC=0Zh5K83dB5qa1IPPVjjVQ2HEqwHRa6514CRYprwFfkM; MMCASM=ID=97B1F0A24A124B1F93E6879994BDB100; ANIMIA=FRE=1; MSCCSC=1; BFBUSR=CMUID=245E56D9FE1D60E101DC42CCFF6161BA; mapc=rm=1; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; _UR=QS=0&TQS=0&cdxcls=0; _tarLang=default=zh-Hans&newFeature=tonetranslation; _TTSS_IN=hist=WyJjeSIsInpoLUhhbnMiLCJlbiIsImF1dG8tZGV0ZWN0Il0=&isADRU=0; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnMiXQ==; EDGSRCHHPGUSR=CIBV=1.1781.0; MSCC=cid=ysg3uej1sj6mmmlp2yqlmm55-c1=2-c2=2-c3=2; _HPVN=CS=eyJQbiI6eyJDbiI6MTQsIlN0IjowLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjE0LCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjoxNCwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wOC0wNVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjo3MSwiVG9ibiI6MH0=; SnrOvr=X=rebateson; tifacfaatcs=CfDJ8Bpr4X1OfMhKmwwJAAtCh6hRJRjMGDWkpoxM4ZSITC8xF4RcdApxiAhQ7woIG80fmvGDGvlbm5cGaYMk0WCPEc1oJMpxBBl2OjfmWSTJ82X7zf3it5y6ELf5_aThnj7neiUTsWLWQiG0EtoNoZ4O6m0v2mdqCVPX-P-kaqVZg8UAzH2XjJoaNuNMQa8q_xSdrP2bWEB3MX322rYj_0yEFxr4Akqb5Z3wKm5TQNQtFiO0HyKnkjHiXdipc2vXPl8aH1uR-nPwtKGHC1ewOelfxGXuvSoUyiHp0BaLmeOw_sRMljesKp5gHWP6fYlHhzl79W708i6PcGMtr2EaFTMHsjoGY7gepyt90OJBv7Ni_0hJo-1eVHT_d7ihJ091ApEZluiagwvv5ENPtv6MolNVXUnIdNEI8XNiPt-FGa7fSpsxFfiJONnhxwVj32w_kDtHRsFntNFjL9rHJNxmxwOL4b9_tr3H3KvsogMyqClwQJx_6zhY5EQxOn6UjqDlu4UM2rv_Fsvl9O3OtWTK_ZKzRyc-knrftmh-SNOq4w2OAGRcvnGH-FZkwROJ9e1jGWxLtiniv9akSMIjcjuHo8sImW80bEmbbw6ByT_UMiO6hfy1hU0bafncAvmAspIlTGT2S3V4X2dFuKuI_o_R11Vgx9Df6YdKbufO2jzf3_lYBYRdJRw4fW--6xztkBpFWOZfTjDN1Dc8T7CbKJ76HSGQSDlZbuvbfwXJhdbeiyrtu9qsDYyYyhQQTWUoeg-jhXzfm7_pIh7zYMqNrjgYhNaVwFgsaz-NoBxQufveW3kYtH1RFBjAtzeI-dzoxZFUnETWcJnbdejsV5Ec-fn1mhJ-IsTip2AjiBYGGVJbjuPoOhh59rK0e4RaEhdlXKHCzpr_9NfrPL4e87nKJIT1q2TfPcH4t4f5ZEkKRSxJmiSebMwYVhcLXJkkbs8z3oFsNttguzyVDZLvGGEqjsnNdPdhcTIK6UEh8X7FRwqR_GkMvszSubJxQ1E01qCwODMaMnhxaDnKuUzGH0DNz619X8ywCSaYG1uXS_C1y43Vvw20viP8ANX89GTYB3erNqRn_bVXwc83mQ_0abnVNhxayFfuw8Hy2VQLIGhmiLa4o0jDoR_pbA9NPx727OPiQotlDbSJqZc-l9we1crK71uB0KS_F-1m89LH-oAXjsE8gAXqAVuEe8sIkvccJKwS1ya5u2NivMoqB0j3xH_ShddAHs-Zk0mJd97RuxxhAOcat2XwjoqFOPha9xJzgzPFVGZh1sQ18DXFmblvjn40WKor_D8vuqrOqIguOJll2QupdjipldHDLM-3vx8VzsES53985Evh0EHTIhhAG5BDfl4-tAoardA2zoVWy5Z2n7-AKVy_2pRF7iVp_jMmLxNx0wRjdby9k4vk5atfLSK2p2KV51_WYXf_5WmS3SoeOl0e6hPYDIiutESn_aaomrkk8kuRg6wX27fbGGVpDuKoUHxGCM_sq0ycaXk3HFcDz18sBS20czW2MJj5Wi3RflFazZSbHhnIEVDh1IlaWb5BilAR-me6fva1i18oTtB1piRXUxzZHDIXuURrn1ZPfQA_bToqDRrqNqgTNurHPCbVy3-yMowInpyET4-y7UiBdJtkKNlvbPBIHmWYHWG94H9YUwecPmbvQHCDglIyww1-qeVM8g2ISmSmKlQ4PEBfyvfo1VocUstcnsHQs0zMsbZyNIIBNGJ9UognrGlppnipBMDGLVMOT1u9TAoF7t-F4xkgkuFnAkEv12SnEOxFCWtTEBOrgmaLNtJgnCG9XbqIwXthwHsRA6XDWZECxX3DbqYmAUZNotQIre7PcUbUJrUVTERUiTzctEVhipQSzCOnp4yW4X2uatuJjBLjtdPXJz1-SBb5JlKGDxB_oDBq8exofJeydVbYyJBAaFaEM0whw7p8ZxxnVQK302aV3sgdzKCqcCtDJ0tRZ6NlA1G1zLfvIMzxmOd8-tv-Cv_misQKMeOcTDeNi7nrHXtl5JmQHv3L66VO6BePbgeiz3t-4OuouDl1yPTG0oOUtF-YEy9mH-hVNONO4v2-_Gqortxy3EQCg37eVr5vlpSyW0Ds29oMLuCuKvN-vps82R96q2WqwUllJZjicjLNqDlLxNuBKMeG7JecmMRbWWAXJRgciLa4OilzMLm4FnZz5uVAccMzPTxIwurSbNeOCDxrYxybXLob4Q9ug-ik2Gejr-SpPKxdudgC6PISRTWSZp5W8RqtI2_5JEMi0YhG460HQsASTpPyCqB2UG8tlEaYmO-bbwAyVCHo_A3pGtUydjcPAMbJ5GK6pmzERiBdVu6x11h9WgJkEAvFsgWjAPRcybxzfTBcCNsYD2jbuX4HQG601x21AhBLRsVxO2TsJEqJV12uE_JjG_c66lWBRtTt8RXDjFx7tPkgCmDLigS8ORzJQicphHhZiJ45ZjRydM_GFyzdg4SsMsDySVeb7TNJshbZ1X19sCNMcbYa1LmngysNHxtH8nn6799h0Q7GQmSHfiXXYl5REXqPADCoWIH9Tj7CJ-apuvqO5Z8WoY6c6zWFkbK15I6BoPBs29XCFJFHUE-SHMAD_XjYxEXZBCJL8JcO3ALANrIDztTOkLuxskxoLpMffEbvY-dMGp4p8_Oed4sT4NdEYSpYINAdy8uU3L9O14acEJgOrYOKR21QtmSK9WvxQ5-QYjVlxXVmO-YcOylywqvfo7MS72Wsd9kFuc5ihMCeVfWYv5VurxkdiS7Vck5Oscv4H4-hNYcKi_IL03sxRlBQhHglWMCpMw1THkVUBu8mlDlI_YxkvHHCTPoMAi-tSzxS7hZnQeND3Rahn5Ob3oQ9JTPD-wkWMwOx_PVfjs90jcv1z-YI4OO-9OfOLkqrJEgLSEdqcuEBHYSg_Ot-1YVUs8Eg7gsvff3aH8ni2pe-fOTL3WY7RrE7qs3pPLl-3lWO6lM7igqPgKv9OC2bCtXDmxwFkFuYtU5YzDOxFBjgqhLvrsYRZnCSsrXNexaR-Vb4yM50ShBXKLMhpC1VcZgjVZSL_8o8OSTu8M0En1rXeEOzJgYLE8iEX43oWZ59pI2lBjF-NIAgrxww9Uigxi9iwirIBFMoauEfTdtb-zE_oVXPd_KOg-JGIMbfWnksxYz95u45mTChMqxHQtU2tivFP974UKXUphzu2h8XviFGWYQH-He5lyC0T15SoXv-1gajBVA4Pn8-sDIG7Tm3qVwhtLruTG_42FmFdzkLS7Ye3H1QmEEL2gWiZud9srRN_Uk58qwlnG_JJWlQmcqw9I7xT5DWss7DhGpnm9NIbWNBFddngvumr5ARocjJcKaJpENccugDEB4Zd4myxELV2Yp9mdQSQ-dFU7liwNO1JJ6s39QxK7i76GY0YT76y5UjhtpCTzzpg8sKNm6Zlw9z7PB_1dS_d5FtNF3milXDp6ZJzoc6Qyhbu_Bu-F3iBmW88fEaHEh3PNvuf3WNrIvYfammjtSsZWKdgxFySRJ0mMv1h5MWrRfe2IM7ja-DXLo_nmgXp35I5boxqRW2szVhVTgXE7_JyyyYn-24PDgCXDbbtIW-W_RUzF5cCb40EovfQ5I-y-MqNOCUMc7wl_JjyKlaZ9yqQ4l18jmXClvcffAG6_kaCubwS7_MNAFTpiaV7817GELQW5e0_SqabaoOGfif8_TgKIu7KDa34lsVzniUqv-vWx31G_EGeVmkVubd1aFe4NaanExPIlaNE4MB7OQDmolbS1h8Xg0_Sf2LMfFJ7RPQIbLC1GLinzmeEgVy3wbmk3HgL5gMpNagMr7Idli4Em2T89TXoHaOdWjaEEWd6AjsWS0PHG8E2Hh9BaWlCu1pXb1cMF2YX7p4hzCVxNGcsX8wXEzR; _clck=1g53ira%7C2%7Cfoq%7C1%7C1489; USRLOC=HS=1&ELOC=LAT=34.57088088989258|LON=105.69159698486328|N=%E7%A7%A6%E5%B7%9E%E5%8C%BA%EF%BC%8C%E7%94%98%E8%82%83%E7%9C%81|ELT=2|&CLOC=LAT=34.57157122676627|LON=105.69122576970088|A=733.4464586120832|TS=240830000040|SRC=W&BID=MjQwODMwMDgwMDM5X2I1ZDg5MDQ2ZjFlYTQ0M2ViOTgwMDdlMDkxY2E0YmU2MTdmNTEwYjZmNWMyNDBlNGRjODEzMmViMmIxYTViNzU=; _uetsid=77a6b9d0634111ef8fef358128b71914; _uetvid=73b77110be7511ee8c9783dd393862f3; _clsk=2q4sdh%7C1724916566769%7C7%7C0%7Cw.clarity.ms%2Fcollect; SRCHUSR=DOB=20240129&T=1724924123000&POEX=W; SRCHHPGUSR=SRCHLANG=zh-Hans&DM=1&PV=10.0.0&BZA=0&HV=1724924127&BRW=XW&BRH=M&CW=1912&CH=930&SCW=1897&SCH=2564&DPR=1.0&UTC=480&EXLTT=31&PRVCW=1912&PRVCH=930&IG=B83ED4DD44CE4466A5B91E4EE7995BB0&THEME=1&PR=1&cdxupdttm=638450858501228047&CIBV=1.1773.0&OR=0&CMUID=245E56D9FE1D60E101DC42CCFF6161BA&WEBTHEME=1&AV=14&ADV=14&RB=1721894369381&MB=1721894369384; _RwBf=r=1&ilt=0&ihpd=0&ispd=0&rc=5129&rb=5129&gb=0&rg=17915&pc=5024&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=3&l=2024-08-29T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-08-29T00:28:43.2556333-07:00&o=16&p=BINGTRIAL5TO250P201808&c=MY00IA&t=4759&s=2023-01-13T09:37:59.7422461+00:00&ts=2024-08-29T09:35:26.0789881+00:00&rwred=0&wls=0&wlb=0&wle=0&ccp=2&lka=0&lkt=0&aad=0&TH=&mta=0&e=cH_hqXk6Ob-rxu8ULeNcECLJxqLekA_08yviimXYBWDAGJZKukNQplKaqfZKYStbBPVXmGTrHfrBAs2DZYC-LQ&A=52551A6B753C52BCDDDBD4D3FFFFFFFF&rwflt=2024-08-26T03:50:56.5068348-07:00&cpt=0; _EDGE_S=SID=3F143504C8776390017121EFC9596200; SNRHOP=I=&TS=; WLS=C=00829e7a37c416a0&N=%e5%ba%86%e6%b5%a9; _SS=SID=3F143504C8776390017121EFC9596200; _U=1uIy4GSDix-xzFVCFiJMj0nxzREjbbbXLxM2r0-_-n9RAYYIiX9I8xUNyGuGKf92FdRxXuxIJdLeiq6hmK49sTc4qaOlqgVv2yAFNQ_-pEV_Xd691pghkwLpus8iYusUuSwHMe78N6Wv6NdbX3W9ep3nCVoGvBQ61H_Mp4umh1vvXAVk6Bu1umLRJbCR71y390Z38bAZHyQCuqnFhkuli7o6X_npUkcfWBhL9y12H9Bs; GRNID=dcd103e6-7501-45cc-900b-30d2d67bfc82; _C_Auth=; GC=lptsJ1pGEHUuZiqHH-K6gnSYfyQu-cXDXpfHFEnSU6VlspOlGbYNhd4PLyEqqSeZyuGKe8Le-e9ndUl3GASbJQ",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        }

        resp = requests.get(url, headers=headers).json()
        computer_balance = int(resp['dashboard']['userStatus']['counters']['pcSearch'][0]['attributes']['progress'])
        mobel_balance = int(resp['dashboard']['userStatus']['counters']['mobileSearch'][0]['attributes']['progress'])
        return computer_balance, mobel_balance
    except Exception as e:
        print(e)
        return 0, 0


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
        };
        # print(proxies["http"], proxies["https"])
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
    # if activeLevel == 'Level1':
    #     # pc端搜索10次
    #     for i in range(10):
    #         q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
    #         printLog(f'电脑搜索第{i + 1}次', bing_rewards(q_str, bingCK, 1))
    #         rand = random.randint(4, 5)
    #         time.sleep(rand)
    #         new_Balance = getBalance(bingCK)
    #         printLog(f'积分', new_Balance)
    #         if bingDetectionStop != 'false':
    #             if getBalanceGap(old_Balance, new_Balance) <= 0:
    #                 printLog('检测', '积分未变动，停止运行！')
    #                 break
    #             old_Balance = new_Balance
    # else:
    #     # pc端搜索35次
    #     for i in range(35):
    #         q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
    #         printLog(f'电脑搜索第{i + 1}次', bing_rewards(q_str, bingCK, 1))
    #         rand = random.randint(4, 5)
    #         time.sleep(rand)
    #         new_Balance = getBalance(bingCK)
    #         printLog(f'积分', new_Balance)
    #         if bingDetectionStop != 'false':
    #             if getBalanceGap(old_Balance, new_Balance) <= 0:
    #                 printLog('检测', '积分未变动，停止运行！')
    #                 break
    #             old_Balance = new_Balance
    #         # 安卓端搜索20次
    #     for i in range(20):
    #         q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
    #         printLog(f'安卓搜索第{i + 1}次', bing_rewards(q_str, bingCK, 0))
    #         rand = random.randint(4, 5)
    #         time.sleep(rand)
    #         new_Balance = getBalance(bingCK)
    #         printLog(f'积分', new_Balance)
    #         if bingDetectionStop != 'false':
    #             if getBalanceGap(old_Balance, new_Balance) <= 0:
    #                 printLog('检测', '积分未变动，停止运行！')
    #                 break
    #             old_Balance = new_Balance

    # # pc端搜索35次
    # for i in range(35):
    #     q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
    #     printLog(f'电脑搜索第{i + 1}次', bing_rewards(q_str, bingCK, 1))
    #     rand = random.randint(4, 5)
    #     time.sleep(rand)
    #     new_Balance = getBalance(bingCK)
    #     printLog(f'积分', new_Balance)
    #     if bingDetectionStop != 'false':
    #         if getBalanceGap(old_Balance, new_Balance) <= 0:
    #             printLog('检测', '积分未变动，停止运行！')
    #             break
    #         old_Balance = new_Balance
    # # 安卓端搜索20次
    # for i in range(20):
    #     q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
    #     printLog(f'安卓搜索第{i + 1}次', bing_rewards(q_str, bingCK, 0))
    #     rand = random.randint(4, 5)
    #     time.sleep(rand)
    #     new_Balance = getBalance(bingCK)
    #     printLog(f'积分', new_Balance)
    #     if bingDetectionStop != 'false':
    #         if getBalanceGap(old_Balance, new_Balance) <= 0:
    #             printLog('检测', '积分未变动，停止运行！')
    #             break
    #         old_Balance = new_Balance

    computer_balance, mobel_balance = get_today_balance()
    printLog('今日电脑积分', str(computer_balance))
    printLog('今日手机积分', str(mobel_balance))
    count = 1
    c_count = 1
    m_count = 1
    while computer_balance != 90:
        q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
        printLog(f'电脑搜索第{count}次', bing_rewards(q_str, bingCK, 1))
        rand = random.randint(4, 5)
        time.sleep(rand)
        new_Balance = getBalance(bingCK)
        printLog(f'积分', new_Balance)
        computer_balance, mobel_balance = get_today_balance()
        printLog('今日电脑积分', str(computer_balance))
        count += 1
        c_count += 1
        if c_count > 100:
            print(f"电脑搜索次数大于{c_count} 直接退出此次搜索")
            break
    while mobel_balance != 60:
        q_str = urllib.parse.quote(get_random_char().encode('utf-8'))
        printLog(f'安卓搜索第{count}次', bing_rewards(q_str, bingCK, 0))
        rand = random.randint(4, 5)
        time.sleep(rand)
        new_Balance = getBalance(bingCK)
        printLog(f'积分', new_Balance)
        computer_balance, mobel_balance = get_today_balance()
        printLog('今日手机积分', str(mobel_balance))
        count += 1
        m_count += 1
        if m_count > 100:
            print(f"手机搜索次数大于{m_count} 直接退出此次搜索")
            break

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
    # url = "https://service.ipzan.com/core-extract?num=1&no=20230930146331307287&minute=3&format=json&protocol=1&pool=quality&secret=daogee708nejt4g"
    # r = requests.get(url)
    # r = json.loads(r.text)
    # proxies["http"] = f'{r["data"]["list"][0]["ip"]}:{r["data"]["list"][0]["port"]}'
    # proxies["https"] = f'{r["data"]["list"][0]["ip"]}:{r["data"]["list"][0]["port"]}'
    # print(proxies["http"], proxies["https"])
    bingCK = "MUID=245E56D9FE1D60E101DC42CCFF6161BA; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=7C5B10AF77A34837AEEA49823FD9D42F&dmnchg=1; ANON=A=52551A6B753C52BCDDDBD4D3FFFFFFFF; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; MUIDV=NU=1; MSPTC=0Zh5K83dB5qa1IPPVjjVQ2HEqwHRa6514CRYprwFfkM; SnrOvr=X=rebateson; MMCASM=ID=97B1F0A24A124B1F93E6879994BDB100; ANIMIA=FRE=1; MSCC=cid=mtafqyq8rwmj6woos8t16wsy-c1=2-c2=2-c3=2; MSCCSC=1; EDGSRCHHPGUSR=CIBV=1.1655.1; _clck=1g53ira%7C2%7Cfkm%7C1%7C1489; _EDGE_S=SID=3EEC5AF360EE660B2DE04EA561A46700; WLS=C=00829e7a37c416a0&N=%e5%ba%86%e6%b5%a9; SRCHS=PC=CNNDDB; USRLOC=HS=1&ELOC=LAT=34.57357406616211|LON=105.69229125976562|N=%E7%A7%A6%E5%B7%9E%E5%8C%BA%EF%BC%8C%E7%94%98%E8%82%83%E7%9C%81|ELT=2|&CLOC=LAT=34.574992519220686|LON=105.69330240969846|A=733.4464586120832|TS=240403070558|SRC=W&BID=MjQwNDAzMTUwNTU3X2I1ZDg5MDQ2ZjFlYTQ0M2ViOTgwMDdlMDkxY2E0YmU2MTdmNTEwYjZmNWMyNDBlNGRjODEzMmViMmIxYTViNzU=; _Rwho=u=d&ts=2024-04-03; dsc=order=BingPages; _U=11V2UtoiLrmwdHjSW5ViVX1YQj9ZsQPiAYRdPgLuJnx2dV31n2SMDpTedj633n6ZkVWLhlhJdfUZfZv1jlmIcZbxyTbcSaywW5Z_CRF9cOeSC2ZFhEDCYEYcj6VIkcky3JwBhTezYUWt3rIdxpaDqO-3XWh8MS6wA_SRhL6R_xTAMSyMB5QijBFCWb_OaLtx4DSJC9f-6eA38MMkE4SQND2QYcF0N1o2YqEpATGVwPq0; _uetsid=1179e8e0f15311ee8854f728cf9d8af5; _uetvid=73b77110be7511ee8c9783dd393862f3; _C_ETH=1; GC=lptsJ1pGEHUuZiqHH-K6gnSYfyQu-cXDXpfHFEnSU6WYKs545adR3cPtMhMBjsNVBpjRrxajAQR-h5XP1aU4Zw; _clsk=pjrg83%7C1712127898326%7C5%7C0%7Cb.clarity.ms%2Fcollect; SNRHOP=I=&TS=; SRCHUSR=DOB=20240129&T=1712128132000&POEX=W; ipv6=hit=1712131734996; _UR=QS=0&TQS=0; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wNC0wM1QwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoxLCJUb2JuIjowfQ==; _RwBf=r=1&ilt=0&ihpd=0&ispd=0&rc=12771&rb=12771&gb=0&rg=35830&pc=12662&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=1&l=2024-04-03T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-04-02T23:53:58.3482049-07:00&o=16&p=BINGTRIAL5TO250P201808&c=MY00IA&t=4759&s=2023-01-13T09:37:59.7422461+00:00&ts=2024-04-03T07:08:55.4298519+00:00&rwred=0&wls=0&wlb=0&wle=0&ccp=0&lka=0&lkt=0&aad=0&TH=&mta=0&e=cH_hqXk6Ob-rxu8ULeNcECLJxqLekA_08yviimXYBWDAGJZKukNQplKaqfZKYStbBPVXmGTrHfrBAs2DZYC-LQ&A=&rwflt=2024-03-28T02:37:02.2187588-07:00; _SS=SID=3EEC5AF360EE660B2DE04EA561A46700&PC=CNNDDB&R=12771&RB=12771&GB=0&RG=35830&RP=12662; SRCHHPGUSR=SRCHLANG=zh-Hans&DM=1&PV=10.0.0&BZA=0&HV=1712128212&BRW=NOTP&BRH=M&CW=817&CH=932&SCW=802&SCH=932&DPR=1.0&UTC=480&EXLTT=31&PRVCW=1912&PRVCH=932&IG=8EE35A8F70CD4CD38F07C5AC933CB322&THEME=1&PR=1&cdxupdttm=638450858501228047&CIBV=1.1633.0"
    # bingCK = "MUID=245E56D9FE1D60E101DC42CCFF6161BA; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=7C5B10AF77A34837AEEA49823FD9D42F&dmnchg=1; ANON=A=52551A6B753C52BCDDDBD4D3FFFFFFFF; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; MUIDV=NU=1; MSPTC=0Zh5K83dB5qa1IPPVjjVQ2HEqwHRa6514CRYprwFfkM; MMCASM=ID=97B1F0A24A124B1F93E6879994BDB100; ANIMIA=FRE=1; MSCCSC=1; BFBUSR=CMUID=245E56D9FE1D60E101DC42CCFF6161BA; MicrosoftApplicationsTelemetryDeviceId=bd95cd5f-5a4c-439e-a188-ef3ec9ff69ff; mapc=rm=1; SnrOvr=X=rebateson; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; _UR=QS=0&TQS=0&cdxcls=0; EDGSRCHHPGUSR=CIBV=1.1759.0; MSCC=cid=eurd46gtpkn8n70iyxwibnzd-c1=2-c2=2-c3=2; _tarLang=default=zh-Hans&newFeature=tonetranslation; _TTSS_IN=hist=WyJjeSIsInpoLUhhbnMiLCJlbiIsImF1dG8tZGV0ZWN0Il0=&isADRU=0; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnMiXQ==; _uetvid=73b77110be7511ee8c9783dd393862f3; _EDGE_S=SID=0F417946D94E65D12C126DE4D89C64BD; WLS=C=00829e7a37c416a0&N=%e5%ba%86%e6%b5%a9; _U=1LQ-wzXXcXoCxPZQT6WYutHZ-gmQnfjCVOW27ePyPhwnEEZBYZrOuodcsjk0JDV5xDPPA93IWH2DJ7JXeSzex86CbSM_7GQ-2iMbYVH0JAzw1fk9uk1i1Jf0e8khWBlN5iEw3BpeSU8ry5Xv-mHP5FYXPq45WW4VCJoiszkj8aWZvHBz3frMjjF-I8-uHP8mzbh20alWvmWRmo9z7T7px5rWGmREnpld93qvDllocpYE; _clck=1g53ira%7C2%7Cfmq%7C1%7C1489; _clsk=143mm2c%7C1718669919212%7C2%7C1%7Cw.clarity.ms%2Fcollect; SRCHS=PC=CNNDDB; USRLOC=HS=1&ELOC=LAT=34.56698989868164|LON=105.69557189941406|N=%E7%A7%A6%E5%B7%9E%E5%8C%BA%EF%BC%8C%E7%94%98%E8%82%83%E7%9C%81|ELT=2|&CLOC=LAT=34.566989368119096|LON=105.69556928412115|A=733.4464586120832|TS=240618000603|SRC=W&BID=MjQwNjE4MDgwNjAzX2I1ZDg5MDQ2ZjFlYTQ0M2ViOTgwMDdlMDkxY2E0YmU2MTdmNTEwYjZmNWMyNDBlNGRjODEzMmViMmIxYTViNzU=; SRCHUSR=DOB=20240129&T=1718669999000&POEX=W; SNRHOP=I=&TS=; _Rwho=u=d&ts=2024-06-18; _HPVN=CS=eyJQbiI6eyJDbiI6MTIsIlN0IjowLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjEyLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjoxMiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wNi0xOFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjo2NCwiVG9ibiI6MH0=; ai_session=hNGAt9cGZw3soBIP6WFmfH|1718670003819|1718670003819; _C_ETH=1; GC=lptsJ1pGEHUuZiqHH-K6gnSYfyQu-cXDXpfHFEnSU6VWctyelstyBMmHBa_MNOsfu-KBmETf-p_SejJkZzHSFQ; _RwBf=r=1&ilt=0&ihpd=0&ispd=0&rc=8019&rb=8019&gb=0&rg=17915&pc=8019&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=20&l=2024-06-17T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=2024-06-16T17:07:42.8223197-07:00&o=16&p=BINGTRIAL5TO250P201808&c=MY00IA&t=4759&s=2023-01-13T09:37:59.7422461+00:00&ts=2024-06-18T00:20:03.9597853+00:00&rwred=0&wls=0&wlb=0&wle=0&ccp=2&lka=0&lkt=0&aad=0&TH=&mta=0&e=cH_hqXk6Ob-rxu8ULeNcECLJxqLekA_08yviimXYBWDAGJZKukNQplKaqfZKYStbBPVXmGTrHfrBAs2DZYC-LQ&A=&rwflt=2024-06-17T08:27:43.9549240-07:00&cpt=0; _SS=SID=0F417946D94E65D12C126DE4D89C64BD&PC=CNNDDB&R=8019&RB=8019&GB=0&RG=17915&RP=8019; ipv6=hit=1718673605564; SRCHHPGUSR=SRCHLANG=zh-Hans&DM=1&PV=10.0.0&BZA=0&HV=1718670021&BRW=NOTP&BRH=M&CW=356&CH=932&SCW=341&SCH=932&DPR=1.0&UTC=480&EXLTT=31&PRVCW=1912&PRVCH=932&IG=7237D47E35C643C1BAEC651E00F7C5CA&THEME=1&PR=1&cdxupdttm=638450858501228047&CIBV=1.1732.0&OR=0&CMUID=245E56D9FE1D60E101DC42CCFF6161BA&WEBTHEME=1"
    # bingCK = "MUID=245E56D9FE1D60E101DC42CCFF6161BA; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=7C5B10AF77A34837AEEA49823FD9D42F&dmnchg=1; ANON=A=52551A6B753C52BCDDDBD4D3FFFFFFFF; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; MUIDV=NU=1; MSPTC=0Zh5K83dB5qa1IPPVjjVQ2HEqwHRa6514CRYprwFfkM; MMCASM=ID=97B1F0A24A124B1F93E6879994BDB100; ANIMIA=FRE=1; MSCCSC=1; BFBUSR=CMUID=245E56D9FE1D60E101DC42CCFF6161BA; MicrosoftApplicationsTelemetryDeviceId=bd95cd5f-5a4c-439e-a188-ef3ec9ff69ff; mapc=rm=1; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; _UR=QS=0&TQS=0&cdxcls=0; _tarLang=default=zh-Hans&newFeature=tonetranslation; _TTSS_IN=hist=WyJjeSIsInpoLUhhbnMiLCJlbiIsImF1dG8tZGV0ZWN0Il0=&isADRU=0; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnMiXQ==; EDGSRCHHPGUSR=CIBV=1.1781.0; MSCC=cid=ysg3uej1sj6mmmlp2yqlmm55-c1=2-c2=2-c3=2; SnrOvr=X=rebateson; _EDGE_S=SID=1E5791AB584068133443857959C3697E;"
    # bingCK = "MUID=245E56D9FE1D60E101DC42CCFF6161BA; _EDGE_V=1; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=7C5B10AF77A34837AEEA49823FD9D42F&dmnchg=1; ANON=A=52551A6B753C52BCDDDBD4D3FFFFFFFF; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; MUIDV=NU=1; MSPTC=0Zh5K83dB5qa1IPPVjjVQ2HEqwHRa6514CRYprwFfkM; MMCASM=ID=97B1F0A24A124B1F93E6879994BDB100; ANIMIA=FRE=1; MSCCSC=1; BFBUSR=CMUID=245E56D9FE1D60E101DC42CCFF6161BA; MicrosoftApplicationsTelemetryDeviceId=bd95cd5f-5a4c-439e-a188-ef3ec9ff69ff; mapc=rm=1; MUIDB=245E56D9FE1D60E101DC42CCFF6161BA; _UR=QS=0&TQS=0&cdxcls=0; _tarLang=default=zh-Hans&newFeature=tonetranslation; _TTSS_IN=hist=WyJjeSIsInpoLUhhbnMiLCJlbiIsImF1dG8tZGV0ZWN0Il0=&isADRU=0; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnMiXQ==; EDGSRCHHPGUSR=CIBV=1.1781.0; MSCC=cid=ysg3uej1sj6mmmlp2yqlmm55-c1=2-c2=2-c3=2; SnrOvr=X=rebateson; _EDGE_S=SID=1E5791AB584068133443857959C3697E; WLS=C=00829e7a37c416a0&N=%e5%ba%86%e6%b5%a9; _U=1lsnfM0r-YKfWj9gEcLVJReB-Hsnb2jLNA0XU-g46C39z1WtB4Il5hiwxd1A1y7i4sB8OyHcQcXo5e3PXdkASsjJvO5M7ukzpffuoetUDC8z1u1143zp9CE-RTWDkE3pTEVHdZexoB44MZwyA_FTyorTPfC0uU1lotM5dnjES0VTWXXZR34A9UQc36OM0Jnk0V0gJ04hiA9sPpoE8s8_abkwHMj5CeG-TeLrLgxN1KeY; _clck=1g53ira%7C2%7Cfo2%7C1%7C1489; _uetsid=ee95127052c011ef9685195f552842ea; _uetvid=73b77110be7511ee8c9783dd393862f3; _clsk=kc28b1%7C1722817416806%7C3%7C1%7Ch.clarity.ms%2Fcollect; SNRHOP=I=&TS=; USRLOC=HS=1&ELOC=LAT=34.56694412231445|LON=105.69583129882812|N=%E7%A7%A6%E5%B7%9E%E5%8C%BA%EF%BC%8C%E7%94%98%E8%82%83%E7%9C%81|ELT=2|&CLOC=LAT=34.56694470445438|LON=105.69582917422917|A=733.4464586120832|TS=240805001615|SRC=W&BID=MjQwODA1MDgxNjEzX2I1ZDg5MDQ2ZjFlYTQ0M2ViOTgwMDdlMDkxY2E0YmU2MTdmNTEwYjZmNWMyNDBlNGRjODEzMmViMmIxYTViNzU=; SRCHUSR=DOB=20240129&T=1722817542000&POEX=W; _Rwho=u=d&ts=2024-08-05; _HPVN=CS=eyJQbiI6eyJDbiI6MTQsIlN0IjowLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjE0LCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjoxNCwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNC0wOC0wNVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjo3MSwiVG9ibiI6MH0=; ipv6=hit=1722821149016; GC=lptsJ1pGEHUuZiqHH-K6gnSYfyQu-cXDXpfHFEnSU6X39Kv-QcV7-dtRb3iFvFC3Akk3hLRMLEjcr8D11VCBoQ;"
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
