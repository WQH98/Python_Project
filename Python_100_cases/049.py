# 题目：使用lambda来创建匿名函数。

MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print("The maximum number is %d" % MAXIMUM(a, b))
    print("The minimum number is %d" % MINIMUM(a, b))


