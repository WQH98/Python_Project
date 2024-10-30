def demo1():
    a = 6
    b = 100
    print("a --> %d  b --> %d" % (a, b))
    # 解法1 使用其他变量
    c = a
    a = b
    b = c
    print("a --> %d  b --> %d" % (a, b))


def demo2():
    a = 6
    b = 100
    print("a --> %d  b --> %d" % (a, b))
    # 解法2 不使用其他变量
    a = a + b
    b = a - b
    a = a - b
    print("a --> %d  b --> %d" % (a, b))


def demo3():
    a = 6
    b = 100
    print("a --> %d  b --> %d" % (a, b))
    # 解法3 python专有解法
    a, b = b, a
    print("a --> %d  b --> %d" % (a, b))


demo3()
