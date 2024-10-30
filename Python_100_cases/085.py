# 题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
# 程序分析：999999 / 13 = 76923。

if __name__ == "__main__":
    num1 = 13
    i = 1
    start = 9
    flag = 0
    while flag == 0:
        if start % num1 == 0:
            flag = 1
        else:
            start *= 10
            start += 9
            i += 1
    print("%d / %d = %d" % (start, num1, start/num1))
