# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
# 程序分析：请抓住分子与分母的变化规律。


fenmu = 1.0
fenzi = 2.0

array = [fenzi/fenmu]

for i in range(19):
    tmp = fenzi
    fenzi += fenmu
    fenmu = tmp
    array.append(fenzi / fenmu)


result = 0
for i in range(len(array)):
    result += array[i];


print(result)
