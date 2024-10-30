"""
    如果做不了逆向 可以先尝试一下selenium
    缺点就是慢 因为首先要启动浏览器 其次有些网站反爬可以识别到selenium
"""
import time
from selenium.webdriver import Edge


driver = Edge()
driver.get('https://www.linovelib.com/novel/2547/123015.html')
# 获取网页源代码
data = driver.page_source
print(data)
time.sleep(10)

