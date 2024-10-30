import time

from selenium.webdriver import Chrome

driver = Chrome()  # 实例化谷歌浏览器驱动
driver.get('http://www.baidu.com')   # 打开网址
driver.save_screenshot("baidu.png")
# time.sleep(1000)
driver.quit()  # 退出浏览器