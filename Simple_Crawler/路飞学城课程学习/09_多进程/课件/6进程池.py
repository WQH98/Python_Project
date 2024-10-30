from multiprocessing import Pool
import time


def fun1(name):
    print(f'我是{name}开始')
    time.sleep(3)
    print(f'我是{name}结束')


if __name__ == '__main__':
    # p = Pool()  # 实例化进程池  默认为核心数
    p = Pool(2)  # 实例化进程池  默认为核心数
    for i in range(1, 11):  # 创建了10个进程
        p.apply_async(fun1, args=(i, ))  # 把任务添加到进程池
    p.close()  # 关闭进程池
    p.join()  # 进程池等待
    print('over')