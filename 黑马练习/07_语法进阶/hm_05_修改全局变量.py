# 全局变量
num = 10
list = [1, 2, 3, 4, 5]


def demo1():

    list[0] = 2
    # 希望修改全局变量的值 -- 使用 global 声明即可
    # global关键字会告诉解释器这是一个全局变量 再使用赋值语句时 就不会再创建局部变量了
    global num
    num = 99
    print("demo1 ==> %d" % num)
    print(list)


def demo2():

    print("demo2 ==> %d" % num)
    print(list)


demo1()
demo2()
