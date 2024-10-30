from multiprocessing import Process, Queue

def test(q):
    # 子进程放入数据
    q.put('a')
    q.put('b')
    q.put('c')

if __name__ == '__main__':
    q = Queue()
    p = Process(target=test, args=(q, ))
    p.start()
    p.join()
    print(q.get())  # 主进程拿数据
    print(q.get())  # 主进程拿数据
    print(q.get())  # 主进程拿数据
    print(q.get(timeout=3))  # 主进程拿数据