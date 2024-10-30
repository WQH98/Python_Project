import os
import time
from multiprocessing import Process


def fun():
    print('我是fun函数', '进程id',os.getpid(), '进程父id', os.getppid())
    time.sleep(10)


if __name__ == '__main__':
    p = Process(target=fun)
    p.start()  # 开启多进程
    p.join()
    print('lucky is a good man')
    print('over')
