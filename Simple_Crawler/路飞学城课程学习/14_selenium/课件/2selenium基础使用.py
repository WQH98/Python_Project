import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()  # 实例化
driver.get('https://www.gushiwen.cn/')  # 访问古诗文网站

# 使用id查找节点
# txtKey = driver.find_element(By.ID, 'txtKey')
# print(txtKey)  #<selenium.webdriver.remote.webelement.WebElement (session="953d50dc821197e9bd2ce97a7ab66045", element="9f422884-c998-45f2-8274-3414bd3c50db")>
# time.sleep(1)
# 向搜索框中输入数据
# txtKey.send_keys('唐诗')
# 点击搜索
# submit = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/form/input[3]')
# submit.click()  # 点击搜索按钮


# 使用xpath
# txtKey = driver.find_element(By.XPATH, '//*[@id="txtKey"]')
# txtKey.send_keys('唐诗')
# 点击搜索
# submit = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[1]/form/input[3]')
# submit.click()  # 点击搜索按钮

# 匹配所有超链接
# a_list = driver.find_elements(By.TAG_NAME, 'a')
# a_list = driver.find_elements_by_tag_name('a')  # 老版本的写法  作为了解
# print(a_list)
# for a in a_list:
    # 获取href属性
    # print(a.get_attribute('href'))

# 通过超链接的内容进行节点获取
# res = driver.find_elements(By.LINK_TEXT, '唐诗三百')
# print(res)

# 通过class进行查找  只要是是cont值 就都会返回
# res = driver.find_elements(By.CLASS_NAME, 'cont')
# print(res)

# print(driver.page_source)  # 获取页面源代码
