def demo(num_list):

    print("函数内部的代码")

    # 使用方法修改列表的内容
    num_list.append(9)
    print(num_list)
    print("函数代码执行完成")
    

gl_num_list = [1, 2, 3]
demo(gl_num_list)
print(gl_num_list)

