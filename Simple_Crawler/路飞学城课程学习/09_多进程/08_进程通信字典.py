from multiprocessing import Process, Queue, Manager


def run(dic):
    print("子进程放数据")
    dic['name'] = 'tom'
    dic['age'] = '18'


if __name__ == '__main__':
    dic = Manager().dict()
    p = Process(target=run, args=(dic, ))
    p.start()
    p.join()
    print("主进程获取数据", dic)

