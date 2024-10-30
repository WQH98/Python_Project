def demo(num, num_list):

    print("函数内部的参数")

    # 在函数内部 针对参数使用赋值语句 不会修改到外部的实参变量
    num = 100
    num_list = [1, 2, 3]

    print(num)
    print(num_list)
    print("函数执行完成")


gl_num = 99
gl_num_list = [1, 1, 1]
demo(gl_num, gl_num_list)
print(gl_num)
print(gl_num_list)
