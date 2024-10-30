from multiprocessing import Process, Queue, Manager


def run(list):
    print("子进程放数据")
    list.append('tom')
    list.append(18)


if __name__ == '__main__':
    list = Manager().list()
    p = Process(target=run, args=(list, ))
    p.start()
    p.join()
    print("主进程获取数据", list)

