from multiprocessing import Pool
import time


def fun1(name):
    print(f'我是{name}开始')
    time.sleep(3)
    print(f'我是{name}结束')


if __name__ == '__main__':
    p = Pool(2)  # 实例化进程池  默认为核心数
    t_list = list(range(1, 11))  # 传递进去的参数
    # print(t_list)
    p.map(fun1, t_list)  # 任务添加到进程池