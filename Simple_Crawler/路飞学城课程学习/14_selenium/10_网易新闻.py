import random
import time
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By

driver = Edge()
driver.get('https://news.163.com/')


# 首先 写一个程序控制滚动条向下滑动
def window_top_to_bottom(driver, stop_length=None, step_length=1000):
    """
        滑动一个窗口 从顶部滑动到底部
    :param driver: 浏览器设备 
    :param stop_length: 滑动的距离
    :param step_length: 每次的步长
    :return: 
    """
    # 判断能不能滑动的标志位
    top = 0
    # 下面三行代码是因为edge打开时会弹窗个性化
    # 延时一段时间 然后刷新会把个性化刷新掉
    # time.sleep(6)
    # driver.refresh()
    # time.sleep(3)
    while True:
        # 判断当前 stop_length 为真还是为假
        # 也就是是否还有滑动距离
        # if stop_length:
        #     # 判断是否还有滑动的空间
        #     # 比如只有200可以滑动了 但是下一次的步长是300 那么直接滑动到最后
        #     # 这个可以不使用 直接使用下面的停止条件即可
        #     if stop_length - step_length < 0:
        #         driver.execute_script('window.scrollBy(0, {})'.format(stop_length))
        #         break
        #     # 每次减去滚动的距离
        #     stop_length -= step_length
        # 开始滑动
        driver.execute_script('window.scrollBy(0, {})'.format(step_length))
        # 延时一段时间 来等待加载
        time.sleep(random.random() + 0.5)
        # 获取一下当前浏览器滑动条的高度
        check_height = driver.execute_script('return document.documentElement.scrollTop')
        print(check_height, top)
        if check_height == top:
            print("因为 check_height == top 所以停止")
            break
        top = check_height
    print('不再滚动')


for i in range(5):
    try:
        window_top_to_bottom(driver)
        # 走到这里 证明该点击了
        load_more_btn = driver.find_element(By.XPATH, '//*[@id="index2016_wrap"]/div[3]/div[2]/div[3]/div[2]/div[5]/div/a[3]')
        # 这里需要注意 有些点击按钮上面有遮罩 我们看不到 点击会报错 需要JS进行处理
        # load_more_btn.click()
        # 使用JS进行点击
        driver.execute_script('arguments[0].click()', load_more_btn)
        print(f'第{i}次点击')
    except Exception as e:
        print(e)
        print('已经到底了')
        break

print(driver.page_source)

time.sleep(10)

