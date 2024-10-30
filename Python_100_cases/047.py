# 题目：两个变量值互换。

def change_ab(a, b):
    a, b = b, a
    return a, b


if __name__ == "__main__":
    a = 10
    b = 20
    print("a = %d, b = %d" % (a, b))
    a, b = change_ab(a, b)
    print("a = %d, b = %d" % (a, b))

