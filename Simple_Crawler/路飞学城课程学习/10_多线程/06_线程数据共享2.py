"""
    线程之间的全局变量是共享的
"""
import threading
import time

name = 'tom'


def fun1():
    # 这个地方加了阻塞以后 fun2就会先输出name
    # time.sleep(2)
    age = 20
    global name
    name = '马冬梅'
    print(f'我叫{name}, 今年{age}岁', threading.current_thread().name)
    time.sleep(2)


def fun2():
    age = 20
    # 这个地方name取决于是fun1先修改 还是fun2先输出
    print(f'我叫{name}, 今年{age}岁', threading.current_thread().name)
    time.sleep(2)


thr1 = threading.Thread(target=fun1, name='fun1')
thr2 = threading.Thread(target=fun2, name='fun2')
thr1.start()
thr2.start()
thr1.join()
thr2.join()

print('外部获取数据', name)
print('over')

