import time
from multiprocessing import Process


def run1():
    for i in range(5):
        print("运行run1函数")
        # 当前代码是单进程的 会在这里阻塞
        time.sleep(1)


def run2():
    for i in range(5):
        print("运行run2函数")
        # 当前代码是单进程的 会在这里阻塞
        time.sleep(1)


if __name__ == '__main__':
    # 期间杀死任意一个子进程 都不会影响主进程或其他子进程
    # 如果直接杀死主进程 则剩下的所有子进程都会消失
    # 主死子陪葬
    t1 = time.time()
    # 创建的时候函数不能加括号
    # 如果写成了run1() 那么得到的就是函数的返回值
    # 不加括号 直接写run1 得到的是这个函数的对象
    p1 = Process(target=run1)  # 创建子进程P1
    p2 = Process(target=run2)  # 创建子进程P2
    p1.start()  # 开启P1子进程
    p2.start()  # 开启P2子进程
    # 主进程等待子进程执行完毕
    p1.join()  # 阻塞等待P1子进程执行完
    p2.join()  # 阻塞等待P2子进程执行完
    print("下面的代码")
    print(time.time() - t1)
