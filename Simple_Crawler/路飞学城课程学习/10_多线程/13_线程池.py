from concurrent.futures import ThreadPoolExecutor, wait
import time


def fun(i):
    print('开始线程', i)
    time.sleep(2)
    print('结束线程', i)


# 开启线程池 并发5个线程
pool = ThreadPoolExecutor(5)
# 放入线程池
# for i in range(5):
#     # 传参 正常放入就可以
#     pool.submit(fun, i)
# 列表推导式 等同于上方
# tasks = [pool.submit(fun, i) for i in range(5)]
# wait(tasks)
# print('over')
# print(tasks)
# 也可以使用map方法
pool.map(fun, list(range(5)))
