# 题目：按逗号分隔列表

L = [1, 2, 3, 4, 5]
lenl = len(L)

for i in range(lenl - 1):
    print("%s" % L[i], end=",")


print("%s" % L[lenl - 1])
