def demo1():
    # 定义一个局部变量
    # 1>  出生：执行下方代码后，变量被创建
    # 2>  死亡：函数执行完成之后
    num = 10

    print("在demo1内部局部变量的值是 %d" % num)


def demo2():

    num = 99
    print("demo2 ==> %d" % num)


# 在函数内部定义的变量 不能在函数外面使用
# print("%d" % num)


demo1()
demo2()
