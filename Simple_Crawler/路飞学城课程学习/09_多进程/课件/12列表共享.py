from multiprocessing import Process, Manager


def test(l):
    l.append('a')
    l.append('b')
    l.append('c')


if __name__ == '__main__':
    p_list = Manager().list()
    p = Process(target=test, args=(p_list, ))
    p.start()
    p.join()
    print(p_list)