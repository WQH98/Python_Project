# 题目：利用递归方法求5!。
# 程序分析：递归公式：fn=fn_1*4!


def fun(x):
    if x == 1:
        return 1
    return x * fun(x - 1)


print(fun(5))
