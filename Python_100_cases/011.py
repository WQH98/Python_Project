# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....

# 还是斐波那契数列的问题 从第三个月开始 每个月都是前两个月的兔子数量相加

def fun(n):
    if n == 1:
        return 1
    if n == 2:
        return [1, 1]
    result = [1, 1]
    for i in range(2, n):
        result.append(result[-1] + result[-2])
    return result


print(fun(20))
