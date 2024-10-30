from multiprocessing import Process
name = 'lucky'

def test():
    global name
    print(name)
    name = 'lisi'
    print(name)


if __name__ == '__main__':
    p = Process(target=test)
    p.start()
    p.join()
    # test()
    print(name)