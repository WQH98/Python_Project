# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。

def x_square(x):
    return x * x


if __name__ == "__main__":
    while True:
        num = int(input("Please enter a number: "))
        result = x_square(num)
        print("result is %d" % result)
        if result < 50:
            break

