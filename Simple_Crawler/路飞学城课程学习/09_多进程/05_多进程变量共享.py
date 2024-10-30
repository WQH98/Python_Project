import time
from multiprocessing import Process

num = 1


def run1():
    # 声明num为全局变量
    global num
    num = 2  # 更改全局变量num的值为2
    print("run1", num)


if __name__ == '__main__':
    p1 = Process(target=run1)
    p1.start()
    p1.join()
    # 进程间是相互独立的 每个进程都有自己的独立存储
    # 上面最开始的全局变量num是主进程中的 在子进程中改不了这个值
    print("over", num)

