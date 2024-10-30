import threading
import time


def run():
    print("线程开始")
    time.sleep(2)
    print("线程结束")


if __name__ == '__main__':
    t1 = time.time()
    # 单线程大概10秒左右
    # run()
    # run()
    # run()
    # run()
    # run()

    # 多线程
    thr_list = []
    for i in range(5):
        # 创建线程
        thr = threading.Thread(target=run)
        # 开启线程
        thr.start()
        thr_list.append(thr)
    for thr in thr_list:
        # 线程等待
        thr.join()
    # 计算线程时间
    print(time.time() - t1)
    print('over')
