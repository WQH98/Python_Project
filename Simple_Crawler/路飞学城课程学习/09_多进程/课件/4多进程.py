import time
from multiprocessing import Process

def fun1():
    print('我是fun1开始')
    time.sleep(5)
    print('我是fun1结束')


def fun2():
    print('我是fun2开始')
    time.sleep(5)
    print('我是fun2结束')

if __name__ == '__main__':
    t1 = time.time()
    p1 = Process(target=fun1)
    p2 = Process(target=fun2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('over')
    print(time.time() - t1)
    # fun1()
    # fun2()