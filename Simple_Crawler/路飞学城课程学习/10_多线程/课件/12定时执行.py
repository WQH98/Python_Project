import threading
import time

def run():
    print('执行了')


if __name__ == '__main__':
    # 3秒以后干run的活
    t = threading.Timer(3, run)
    t.start()