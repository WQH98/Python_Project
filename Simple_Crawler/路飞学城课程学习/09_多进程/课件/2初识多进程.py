import os
import time
from multiprocessing import Process


def fun():
    print('我是fun函数', '进程id',os.getpid(), '进程父id', os.getppid())
    time.sleep(1000)


if __name__ == '__main__':
    # p = Process(target=fun())  # 注意  fun()  不能加括号！！！！！！！！！！！！
    p = Process(target=fun)
    p.start()  # 开启多进程
    print('lucky is a good man')
    time.sleep(100)
    print('over')
    # print(p)
    # print(fun)
    # print(fun())