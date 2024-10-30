import threading
import time

name = 'tom'


def fun():
    age = 20
    global name
    name = '马冬梅'
    print(f'我叫{name}, 今年{age}岁')
    time.sleep(2)


thr = threading.Thread(target=fun)
thr.start()
thr.join()
print('外部获取数据', name)
print('over')

