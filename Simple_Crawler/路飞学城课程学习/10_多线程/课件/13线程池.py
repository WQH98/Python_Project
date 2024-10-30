import time
from concurrent.futures import ThreadPoolExecutor, wait


def run(i):
    print(f'线程{i}开始执行')
    time.sleep(3)
    print(f'线程{i}结束执行')


if __name__ == '__main__':
    List = [1, 2, 3, 4, 5]
    # pool = ThreadPoolExecutor() # 线程并发个数不给则默认为  (os.cpu_count() or 1) * 5
    pool = ThreadPoolExecutor(3) # 线程并发个数不给则默认为  (os.cpu_count() or 1) * 5
    # 方式1
    # for i in List:
    #     pool.submit(run, i)

    # 简写
    # task_list = [pool.submit(run, i) for i in List]
    # wait(task_list)  # 当前这的目的等待线程池统一执行完毕
    # print('over')

    # map的方式
    pool.map(run, List)