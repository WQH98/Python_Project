# 注意：在开发时 应该把模块中的所有全局变量都定义在函数的上方
# 就可以保证所有的函数都能够正常的访问到每一个全局变量了
num = 10
# 再定义一个全局变量
name = "ming"
# 再定义一个全局变量
title = "xiao"


def demo():

    print("%d" % num)
    print("%s" % title)
    print("%s" % name)


# # 再定义一个全局变量
# title = "xiao"

demo()

# # 再定义一个全局变量
# name = "ming"

