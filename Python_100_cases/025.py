# 题目：求1+2!+3!+...+20!的和。
# # 程序分析：此程序只是把累加变成了累乘。

array = []
for i in range(1, 21):
    tmp = i
    for j in range(1, i):
        tmp *= j
    array.append(tmp)


result = 0
for i in range(20):
    result += array[i]


print(result)
