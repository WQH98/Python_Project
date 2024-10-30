from selenium.webdriver import Chrome
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
        return result["message"]
    return ""


driver = Chrome()
driver.get('https://www.gushiwen.cn/')  # 访问古诗文
# 点击我的
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/a[6]').click()
# 获取用户名  密码  验证码 登陆的节点
username = '793390457@qq.com'
userpass = 'xlg17346570232'

# 获取用户名节点  并输入用户名
driver.find_element(By.ID, 'email').send_keys(username)
# 获取密码节点 并输入密码
driver.find_element(By.ID, 'pwd').send_keys(userpass)

# 获取雁阵吗图片的节点对象  并进行截取  保存为code.png
img_path = 'code.png'
driver.find_element(By.ID, 'imgCode').screenshot(img_path)
# 调用打码平台
result = base64_api(uname='luckyboyxlg', pwd='17346570232', img=img_path, typeid=3)
print(result)
# 获取验证码节点
driver.find_element(By.ID, 'code').send_keys(result)
# 获取登陆节点 进行登陆
driver.find_element(By.ID, 'denglu').click()