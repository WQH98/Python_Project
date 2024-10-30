def sum_2_num(num1, num2):
    """对两个数字的求和"""

    # 可以使用返回值 告诉调用函数一方计算的结果
    # 注意：return就代表返回 后面的代码不会被执行
    return num1 + num2


# 可以使用变量 来接受函数执行的返回结果
sum_result = sum_2_num(23, 20)
print(sum_result)
