
gl_num = 10
# 再定义一个全局变量
gl_name = "ming"
# 再定义一个全局变量
gl_title = "xiao"


def demo():

    # 如果局部变量的名字与全局变量的名字重复
    # PyCharm会在局部变量的名字下面显示一个灰色的虚线
    num = 99

    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)


demo()
