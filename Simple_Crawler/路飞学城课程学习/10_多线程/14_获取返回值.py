from concurrent.futures import ThreadPoolExecutor, wait, as_completed
import time


def run(i):
    print('开始线程', i)
    time.sleep(5)
    print('结束线程', i)
    return i


# 开启线程池
pool = ThreadPoolExecutor(5)
# # 列表推导式
# tasks = [pool.submit(run, i) for i in range(5)]
# # 获取返回值
# for val in as_completed(tasks):
#     # 获取值
#     print(val.result())

# 使用map方法获取返回值
for val in pool.map(run, list(range(5))):
    print(val)

