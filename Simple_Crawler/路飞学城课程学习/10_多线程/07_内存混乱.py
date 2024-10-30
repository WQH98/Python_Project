import threading

i = 0


def sum1():
    global i
    for x in range(10000000):
        i += x
        i -= x
    print('sum1', i)


def sum2():
    global i
    for x in range(10000000):
        i += x
        i -= x
    print('sum2', i)


def sum3():
    global i
    for x in range(10000000):
        i += x
        i -= x
    print('sum3', i)


thr1 = threading.Thread(target=sum1)
thr2 = threading.Thread(target=sum2)
thr3 = threading.Thread(target=sum3)
thr1.start()
thr2.start()
thr3.start()
thr1.join()
thr2.join()
thr3.join()
print(i)
