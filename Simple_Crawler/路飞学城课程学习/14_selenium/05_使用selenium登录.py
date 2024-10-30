import time
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import base64
import json
import requests


def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        #！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]


driver = Edge()
driver.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')

# 查找用户名节点
driver.find_element(By.ID, 'email').send_keys('793390457@qq.com')
# 查找密码节点
driver.find_element(By.ID, 'pwd').send_keys('xlg17346570232')
# 查找验证码图片节点
imgCode = driver.find_element(By.ID, 'imgCode')
# 截图 截取imgCode节点的截图（也就是验证码）
imgCode.screenshot('./05_yzm.png')
img_path = "./05_yzm.png"
result = base64_api(uname='qq2361125846', pwd='dzyjs81A', img=img_path, typeid=3)
# 查找验证码节点
driver.find_element(By.ID, 'code').send_keys(result)
# 查找登录按钮节点
denglu = driver.find_element(By.ID, 'denglu')
# 点击登录按钮
denglu.click()

# 处理cookies
cookies = driver.get_cookies()
json_cookies = json.dumps(cookies)
with open('./05_gsw_cookies.json', 'w', encoding='utf-8') as f:
    f.write(json_cookies)
print('登录成功')
time.sleep(20)
