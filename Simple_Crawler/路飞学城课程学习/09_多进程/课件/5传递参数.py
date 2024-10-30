import time
from multiprocessing import Process

def fun1(name):
    print(f'我是{name}开始')
    time.sleep(5)
    print(f'我是{name}结束')


def fun2(name):
    print(f'我是{name}开始')
    time.sleep(5)
    print(f'我是{name}结束')

if __name__ == '__main__':
    t1 = time.time()
    # 注意一点 传递参数类型为元祖，一个参数的时候需要添加逗号
    # 列表也可以，但是建议使用元祖
    p1 = Process(target=fun1, args=('lucky',))
    p2 = Process(target=fun2, args=('lisi',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('over')
    print(time.time() - t1)
    # fun1()
    # fun2()