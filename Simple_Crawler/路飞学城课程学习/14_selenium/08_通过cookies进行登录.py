import json
import time
from selenium.webdriver import Edge


driver = Edge()

driver.get('https://so.gushiwen.cn/user/collect.aspx')

time.sleep(5)

# 获取cookies值
with open('./05_gsw_cookies.json', 'r') as f:
    gsw_cookies = json.loads(f.read())

# 添加cookies到selenium
for cookie in gsw_cookies:
    cookie_dict = {}
    for k, v in cookie.items():
        cookie_dict[k] = v
    driver.add_cookie(cookie_dict)

# 刷新页面
driver.refresh()

# 使用cookies进行登录
driver.get('https://so.gushiwen.cn/user/collect.aspx')

time.sleep(20)

