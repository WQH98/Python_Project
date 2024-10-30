# 全局变量
num = 10
list = [1, 2, 3, 4, 5]


def demo1():

    list[0] = 2
    # 希望修改全局变量的值
    # 在 python 中 不允许直接修改全局变量的值
    # 如果使用赋值语句 会在函数内部 定义一个局部变量
    # 此处不允许修改应该指不允许赋值，因为在python赋值相当于c中的值传递，
    # 并不能改变原始变量的值。但是名片系统里那个全局变量list不就改了
    num = 99
    print("demo1 ==> %d" % num)
    print(list)


def demo2():

    print("demo2 ==> %d" % num)
    print(list)


demo1()
demo2()
