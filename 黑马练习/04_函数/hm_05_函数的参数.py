def sum_2_num(a, b):
    """对两个数字的求和"""
    return a + b


def sum_10_num(a):
    """输出等于输入加10"""
    return a + 10


def num_num(a):
    """查看形参是否改变实参"""
    a += 10
    print("函数内参数为%d" % a)


a = 10
num_num(a)
print("函数外参数为%d" % a)
