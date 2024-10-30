import threading
import time


def run(i):
    print('子线程开始', threading.current_thread().name)
    print(f'{i}开始干活')
    time.sleep(3)
    print(f'{i}干活结束')


if __name__ == '__main__':
    t1 = time.time()
    # 存储线程对象
    t_list = []
    # 并发执行5个线程
    for i in range(1, 6):
        thr = threading.Thread(target=run, args=(i, ))
        # 线程对象添加到列表中
        t_list.append(thr)
    # 循环开启子线程
    for t in t_list:
        t.start()
    # 循环阻塞子线程
    for i in t_list:
        i.join()
    print('over')
    print(time.time() - t1)

