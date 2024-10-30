import threading
import time


def run():
    # 获取当前线程名称  默认名称Thread-1
    print(threading.current_thread().name)
    print('run函数开始')
    time.sleep(3)
    print('run函数结束')


if __name__ == '__main__':
    th = threading.Thread(target=run, name='lucky-1')
    th.start()
    th.join()  # 阻塞等待  和进程一样的
    print('over')
    # 查看主线程
    # print(threading.main_thread())
    # 查看主线程名称
    print(threading.main_thread().name)