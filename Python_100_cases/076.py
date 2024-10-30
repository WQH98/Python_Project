# 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
# 在Python中 整数除以整数只能得出来整数 所以要用1.0去除
def fun(n):
    if n == 1:
        return 1
    if n == 2:
        return 0.5
    result = 0.0
    if n % 2 == 0:
        for i in range(2, n + 1, +2):
            result += 1.0 / i
    else:
        for i in range(1, n + 1, +2):
            result += 1.0 / i
    return result


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(fun(n))
