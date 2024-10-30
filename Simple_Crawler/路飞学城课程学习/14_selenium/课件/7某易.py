import random
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def scroll_windwo(driver, stop_lengt=None, step_length=2000):
    '''
    使窗口不断向下滚动
    :param driver:
    :param stop_lengt:
    :param step_length:
    :return:
    '''
    while True:
        if stop_lengt:
            if stop_lengt - step_length <= 0:
                # 使用js实现滚动条自动往下走
                driver.execute_script(f'window.scrollBy(0, {stop_lengt})')
                break
            print(stop_lengt)
            # 使用js实现滚动条自动往下走
            driver.execute_script(f'window.scrollBy(0, {step_length})')
            stop_lengt -= step_length   # 每次减去滚动的距离
            time.sleep(0.1)


driver = Chrome()
driver.get('https://news.163.com/')
step_length = 2000  # 每次向下滚动的步长
stop_lengt = 30000   # 向下滚动到当前整个值得时候就不滚了
for i in range(1, 6):
    scroll_windwo(driver, stop_lengt, step_length)  # 先滚一些  把异步的分页加载先加载文 直到出现加载更多按钮
    more = driver.find_element(By.XPATH, '//*[@id="index2016_wrap"]/div[2]/div[2]/div[3]/div[2]/div[5]/div/a[3]')
    # more.click()
    # 无法使用more.click  原因上面有我们看不到的覆盖物 点击会报错
    driver.execute_script('arguments[0].click();', more)
    print(f'第{i}次点击')

print(driver.page_source)   # 获取页面最终源代码