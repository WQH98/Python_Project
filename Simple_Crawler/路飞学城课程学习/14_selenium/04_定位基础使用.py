import time
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By


driver = Edge()
driver.get('https://www.gushiwen.cn/')
# # By.ID  左上角的搜索框
# txtKey = driver.find_element(By.ID, 'txtKey')
# # 向input搜索框输入搜索内容
# txtKey.send_keys('唐诗')
# print(txtKey)

# 给一个不存在的节点
# 会直接报错 提示没有这个节点
# driver.find_element(By.ID, 'xxx')

# 获取所有的超链接a
# urls = driver.find_elements(By.TAG_NAME, 'a')
# for url in urls:
#     # 这样直接打印出来的是element对象
#     # print(url)
#     # 想要直接获取值 可以使用下面的方法
#     print(url.get_attribute('href'))

# 给一个不存在的节点
# 不会报错 返回一个空列表
# urls = driver.find_elements(By.TAG_NAME, 'xxxxx')
# print(urls)

# 使用xpath 右侧的搜索框
# txtKey = driver.find_element(By.XPATH, '//*[@id="txtKey"]')
# txtKey.send_keys('唐诗')
# 错误写法
# txtKey = driver.find_element(By.XPATH, '//*[@id="txtKey"/text()]')

# 找class类
# urls = driver.find_elements(By.CLASS_NAME, 'cont')
# for url in urls:
#     print(url.text)

# 获取页面内容
# print(driver.page_source)

# 找到输入框
txtKey = driver.find_element(By.ID, 'txtKey')
# 向input输入框输入搜索内容
txtKey.send_keys('唐诗')
# 找到点击搜索的按钮
search = driver.find_element(By.XPATH, '//*[@id="search"]/form/input[3]')
# 点击搜索按钮
search.click()


time.sleep(20)

