# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：
# 1、1、2、3、5、8、13、21、34、……。
# 在数学上，费波那契数列是以递归的方法来定义：

# 输出前n个斐波那契数列
def fun(n):
    if n == 1:
        return 1

    if n == 2:
        return [1, 1]

    result = [1, 1]

    # Python支持负数索引
    # 数组中下标为-1 -2的意思是数组的最后1个元素和倒数第2个元素
    for i in range(2, n):
        result.append(result[-1] + result[-2])
        # 与上面的方法等价
        # result.append(result[i - 1] + result[i - 2])
    return result


print(fun(3))
