# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 程序分析：关键是计算出每一项的值。

n = int(input("n = "))
a = int(input("a = "))
tmp = a
result = [a]
ret_sum = 0

for i in range(1, n):
    a += tmp * 10 ** i
    result.append(a)


for i in range(n):
    ret_sum += result[i]


print(ret_sum)

