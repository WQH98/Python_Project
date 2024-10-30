# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。

i = int(input("Please enter the number: "))
array = []
count = 0

while i > 0:
    tmp = i % 10
    array.append(tmp)
    i = int(i / 10)
    count += 1

reversed(array)
# print(array.reverse())
print("count = %d, array = %s" % (count, array))

