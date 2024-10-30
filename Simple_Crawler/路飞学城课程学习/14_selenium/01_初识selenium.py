import time
from selenium.webdriver import Edge


# 创建浏览器对象
# 这是因为浏览器驱动已经放在了解释器文件夹
# 如果没有放在解释器文件夹的话 需要在括号内添加驱动路径
web = Edge()

web.get('https://www.baidu.com')
time.sleep(10)
print(web.title)





