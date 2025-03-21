# 题目：打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# 程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。

for i in range(4):
    for j in range(7):
        if (3 - j <= i) and (j - 3 <= i):
            print("*", end="")
        else:
            print(" ", end="")
    print("", end="\r\n")

for i in range(2, -1, -1):
    for j in range(7):
        if (3 - j <= i) and (j - 3 <= i):
            print("*", end="")
        else:
            print(" ", end="")
    print("", end="\r\n")
