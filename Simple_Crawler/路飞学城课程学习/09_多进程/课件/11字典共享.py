from multiprocessing import Process, Manager


def test(d):
    d['name'] = 'lucky'
    d['sex'] = 'man'


if __name__ == '__main__':
    # 创建了进程通信的字典类型
    p_dict = Manager().dict()
    p = Process(target=test, args=(p_dict, ))
    p.start()
    p.join()
    print(p_dict)