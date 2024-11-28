import requests
import time
import threading

json_datas = [{"cloudID":"86_U3eRpdwmEoXECACV6cSmyo59QVEi0AU57aGtZ9hQnZz_2MBmCOxyjnhT4kA","encryptedData":"pdWHF0uN5XEi6LbQDvySw4ICNCYTjefF9NnP5Z9ZFT0GYtsWD/7pILksEZZfF8OMBJxGo7CeJrrQjeMalMC8cNPC+wePreYISZYhYgLIHxA5zbt5Ql2eQMSvMd82a9pmnYkwVfjbx49lxswDlLQvVlmJ/HVHDBoKKxlPx3g5THe/YpCzWeyxk1wOJwsTsdnTQc+sLBi/W/tEU3EekJetjBpV12QIWDQJUmy3CArsJ2UMYjhP+eOojvl1Nl65Yj1bmWfptCNrRICx9UsoP9GfpfhG7MlKbTNHR+SrpU6z8fKomJD/zFfKSphRj7LVoT3Qghi/gLWKliP5ZTEkDHEzPmOv8iFgEWc18cxBlz9d1QrWWHfwOrl/4KADruoovyYtjftCmCqP4KkvpIWqzelra7CEcrwwx/4WFjPszDHjU+mXYHZ+Ly1qqBaM8JaUyc0h","iv":"bEZ+Hs81IrvjNZxika7ESQ==","signature":"01b5b50dafa2d5255e3a0eb2bdeb70b9c57b5404","userInfo":{"nickName":"微信用户","gender":0,"language":"","city":"","province":"","country":"","avatarUrl":"https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132","is_demote":"true"},"rawData":"{\"nickName\":\"微信用户\",\"gender\":0,\"language\":\"\",\"city\":\"\",\"province\":\"\",\"country\":\"\",\"avatarUrl\":\"https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132\",\"is_demote\":true}","errMsg":"getUserProfile:ok","openid":"o4WMG41rENEG3_YmaHSvJj0uJ-4g","unionid":"oT4Cj0zhqmYouiyd5zpHn82jaDUY"},
              {"cloudID":"86_eA8g4V0mXnIeh_4apVYYbGTw0fyiNH2ClOB4AQfipuMI-R-Kr12lwW8jDzc","encryptedData":"tILQmXyfaaVn5mUzlcfpdNd6aLEcLBzsTheKVqKUColnrPCuc0Cc59ITMSNONThxmBAwaR7anu2lkj1rKYDbQDQ86lC5eBLsKx+64uF0yMB8WwkIwnA6vLsLxa1MK3ayYwUUjg1h1016eDd92ENARf4mVMxgc3iFZrIysnbZS0gITkuh0cHRX+Bf1DEP/BXOZTBtbXEALkPxx6yQQeH7AmtsMN6Om/ABSOkWoW+n+1xT7ERJgYnZZQh/a7w4ZmU1qb9zzio8G/YHqEIUrTHlkP1uQXh9pLoZgn/DcfUkw+vYi27RWP3dSRm8ZNJkKA7zZbmU2VO82+GXF2C2eU2sbwcgWcEN9le0gq8KqpuUPUWHKqpHuv+Yzdp2IOp2MEActQALMmJGiOiOUiJHugILj080vyKcoj5HlnCWpiF0x28UQqb0tegBOEe1lI0uo3jf","iv":"h6zKl0mS1+5XRcN2eChAXg==","signature":"3ba9b6e4087d4210491a33f702e992ece87d56db","userInfo":{"nickName":"微信用户","gender":0,"language":"","city":"","province":"","country":"","avatarUrl":"https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132","is_demote":"true"},"rawData":"{\"nickName\":\"微信用户\",\"gender\":0,\"language\":\"\",\"city\":\"\",\"province\":\"\",\"country\":\"\",\"avatarUrl\":\"https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132\",\"is_demote\":true}","errMsg":"getUserProfile:ok","openid":"o4WMG42vIqH4fGQgxkL6KZNo0060","unionid":"oT4Cj0_dYqmiGELumUNhti7K3Vc0"}]

finished_flag = True
proxies = {'http': "",
           'https': ""}


def proxies_change():
    """
        切换IP线程 150秒切换一次IP
        return: 无
    """
    global finished_flag
    url = "https://service.ipzan.com/core-extract?num=1&no=20230930146331307287&minute=3&format=txt&protocol=1&pool=quality&mode=whitelist&secret=daogee708nejt4g"
    while finished_flag:
        resp = requests.get(url)
        if resp.status_code == 200:
            proxies["http"] = resp.text
            proxies["https"] = resp.text
        print("获取到IP: ", resp.text)
        time.sleep(150)



# 更新token
def update_token(json_data):
    print("开始刷新token")
    headers = {
        "content-length": "1303",
        "xweb_xhr": "1",
        "contenttype": "[object Undefined]",
        "authorization": "",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c04)XWEB/11275",
        "content-type": "application/json",
        "accept": "*/*",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://servicewechat.com/wx27e219ff3142b7c8/63/page-frame.html",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9",
    }
    try:
        resp = requests.post("https://p.xpfarm.cn/treemp/wx.Login/index", headers=headers, json=json_data, proxies=proxies).json()
        if resp["code"] == 1000:
            print("token刷新成功")
            token = resp["data"]["token"]
            return token
        else:
            print("刷新token失败 直接退出")
            exit(0)
    except Exception as e:
        print(e)
        print("刷新token失败 直接退出")
        exit(0)


# 签到
class XP_FARM:
    def __init__(self, authorization):
        self.tree_water = 0
        self.tree_fertilizer = 0
        self.information_url = "https://p.xpfarm.cn/treemp/user.PersonalCenter/getInfo"
        self.information_header = {
            "authorization": authorization,
            "xweb_xhr": "1",
            "user-agent": "Mozilla/5.0 (Linux; Android 11; ONEPLUS A6000 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260145 MMWEBSDK/20240501 MMWEBID/4671 MicroMessenger/8.0.50.2701(0x2800325B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
            "content-type": "application/json",
            "accept": "*/*",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://servicewechat.com/wx27e219ff3142b7c8/63/page-frame.html",
        }
        self.sign_info_url = "https://p.xpfarm.cn/treemp/user.PersonalCenter/getSigninInfo"
        self.tree_info_url = "https://p.xpfarm.cn/treemp/tree.Tasks/getHomePage"
        self.tree_sign_in_url = "https://p.xpfarm.cn/treemp/tree.Tasks/receiveTaskReward"
        self.add_water_url = "https://p.xpfarm.cn/treemp/tree.Tasks/addWater"
        self.add_fertilizer_url = "https://p.xpfarm.cn/treemp/tree.Tasks/addFertilizer"
        self.complete_tasks_url = "https://p.xpfarm.cn/treemp/tree.Tasks/completeTask"
        self.receive_tasks_url = "https://p.xpfarm.cn/treemp/tree.Tasks/receiveTaskReward"
        self.task_headers = {
            "Host": "p.xpfarm.cn",
            "content-type": "application/json",
            "authorization": authorization,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b11) XWEB/9129",
        }

    # 获取登录信息
    def get_information(self):
        print("开始登录")
        try:
            resp = requests.post(url=self.information_url, headers=self.information_header, proxies=proxies).json()
            print(resp)
            mobile = resp["data"]["mobile"]
            nickname = resp["data"]["nickname"]
            integral = resp["data"]["integral"]
            token = resp["data"]["token"]
            unionid = resp["data"]["unionid"]
            openid = resp["data"]["openid"]
            fruit_gold = resp["data"]["fruit_gold"]
            consumption_price2 = resp["data"]["consumption_price2"]
            level_name = resp["data"]["level_name"]
            consumption_price_next = resp["data"]["consumption_price_next"]
            coupon_count = resp["data"]["coupon_count"]
            print(f"{nickname} 登录成功\n手机号 {mobile}\n当前积分 {integral}\n果金 {fruit_gold}\n优惠券数量 {coupon_count}")
        except Exception as e:
            print(e)
            print("登录失败 authorization失效 重新抓")
            exit(0)

    # 签到
    def sign_in(self):
        try:
            resp = requests.post(url=self.sign_info_url, headers=self.information_header, proxies=proxies).json()
            if resp["code"] == 1000:
                nextDay = resp["data"]["nextDay"]
                isSignInToday = resp["data"]["isSignInToday"]
                print(f"已签到 {nextDay} 天")
                if isSignInToday == 1:
                    print("今日已签到")
                else:
                    pass
            else:
                print("签到失败")
        except Exception as e:
            print(e)
            print("签到请求失败")

    # 获取果树信息
    def get_tree_info(self):
        try:
            resp = requests.post(self.tree_info_url, headers=self.information_header, proxies=proxies).json()
            if resp["code"] == 1000:
                type = resp["data"]["type"]
                type_name = resp["data"]["type_name"]
                fertilizer = resp["data"]["fertilizer"]
                water_value = resp["data"]["water_value"]
                fertilizer_value = resp["data"]["fertilizer_value"]
                progress = resp["data"]["progress"]
                self.tree_water = water_value
                self.tree_fertilizer = fertilizer
                print(
                    f"果树当前处于第 {type} 阶段\n当前肥力 {fertilizer}\n当前水量 {water_value}\n当前肥量 {fertilizer_value}\n当前阶段进度 {progress * 100}%")
            else:
                print("解析果树信息失败")
        except Exception as e:
            print(e)
            print("获取果树信息失败")

    # 果树签到
    def tree_sign_in(self):
        try:
            resp = requests.post(self.tree_sign_in_url, headers=self.information_header, proxies=proxies).json()
            # print(resp)
            if resp["code"] == 1000:
                reward = resp["data"]["reward"]
                reward_type_name = resp["data"]["reward_type_name"]
                day_task_id = resp["data"]["day_task_id"]
                print(f"签到成功 第{day_task_id - 4}天 奖励为{reward_type_name}*{reward}")
            else:
                message = resp["message"]
                print(f"签到失败 原因是 {message}")
        except Exception as e:
            print(e)
            print("获取签到失败")

    # 浇水施肥
    def add_water_and_fertilizer(self):
        count = 0
        if self.tree_water > 10:
            print("开始浇水")
            while self.tree_water > 10:
                resp = requests.post(self.add_water_url, headers=self.information_header, proxies=proxies).json()
                if resp["code"] == 1000:
                    type = resp["data"]["type"]
                    progress = resp["data"]["progress"]
                    water_value = resp["data"]["water_value"]
                    fertilizer = resp["data"]["fertilizer"]
                    self.tree_water = water_value
                    print(
                        f"浇水成功 当前阶段{type} 当前成长进度{'%.2f' % (progress * 100)}% 剩余水滴{water_value} 剩余肥力{fertilizer}")
                else:
                    count += 1
                    print(f"浇水失败第{count}次 超过3次退出")
                    if count > 3:
                        print(f"浇水失败第{count}次 退出浇水")
                        break
                time.sleep(3)
        else:
            print("水量不足 无法浇水")
        count = 0
        if self.tree_fertilizer > 0:
            print("开始施肥")
            while self.tree_fertilizer > 0:
                resp = requests.post(self.add_fertilizer_url, headers=self.information_header, proxies=proxies).json()
                if resp["code"] == 1000:
                    fertilizer_value = resp["data"]["fertilizer_value"]
                    fertilizer = resp["data"]["fertilizer"]
                    self.tree_fertilizer = fertilizer_value
                    print(f"施肥成功 剩余肥料{fertilizer_value} 剩余肥力{fertilizer}")
                else:
                    count += 1
                    print(f"施肥失败第{count}次 超过3次退出")
                    if count > 3:
                        print(f"施肥失败第{count}次 退出浇水")
                        break
                time.sleep(3)
        else:
            print("肥量不足 无法施肥")

    # 做任务
    def do_tasks(self):
        print("开始今日任务")

        for id in range(1, 17):
            print(f"开始任务{id}")
            data = {
                "task_id": id
            }
            try:
                resp = requests.post(self.complete_tasks_url, headers=self.task_headers, json=data, proxies=proxies).json()
                if resp["code"] == 1000:
                    print(f"任务完成成功 原因是{resp['message']}")
                else:
                    print(f"任务完成失败 原因是{resp['message']}")
            except Exception as e:
                print(e)
                print(f"任务完成失败 直接退出 查看问题 id={id}")
                exit(0)
            print(f"开始领取任务{id}奖励")
            try:
                resp = requests.post(self.receive_tasks_url, headers=self.task_headers, json=data, proxies=proxies).json()
                # print(resp)
                if resp["code"] == 1000:
                    print(f"任务奖励领取成功 {resp['data']['reward'][0]['reward_type_name']}x{resp['data']['reward'][0]['reward']}")
                else:
                    print(f"任务奖励领取失败 原因是{resp['message']}")
            except Exception as e:
                print(e)
                print(f"任务领取奖励失败 直接退出 查看问题 id={id}")
                exit(0)
            print("3秒后执行下个任务")
            time.sleep(3)


if __name__ == '__main__':
    thread = threading.Thread(target=proxies_change)
    thread.start()
    time.sleep(10)
    for json_data in json_datas:
        xp1 = XP_FARM(update_token(json_data))
        xp1.get_information()
        # xp1.sign_in()
        xp1.get_tree_info()
        xp1.tree_sign_in()
        xp1.do_tasks()
        xp1.get_tree_info()
        xp1.add_water_and_fertilizer()
    finished_flag = False
