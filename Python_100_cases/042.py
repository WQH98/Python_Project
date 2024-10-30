# 题目：学习使用auto定义变量的用法。
# 程序分析：没有auto关键字，使用变量作用域来举例吧。

num = 2


def autofun():
    num = 1
    print("internal block num = %d" % num)
    num += 1


if __name__ == "__main__":
    for i in range(3):
        print("The num = %d" % num)
        num += 1
        autofun()
