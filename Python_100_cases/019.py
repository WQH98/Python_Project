# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
# 程序分析：请参照程序Python 练习实例14。

result = []


def fun(num):
    tmp = 0
    i1 = 2
    sign = 0
    while i1 < num:
        tmp = num / i1

        if tmp.is_integer():
            # print(i, end="\t")
            result.append(i1)
        #     num = tmp
        #     sign = 1
        # if sign == 1:
        #     sign = 0
        # else:
        #     i1 += 1
        i1 += 1
    return result


for i in range(2, 1001):
    tmp1 = fun(i)
    sum_tmp = 1
    for j in range(len(tmp1)):
        sum_tmp += tmp1[j]
    if i == sum_tmp:
        print(i)
        tmp1.insert(0, 1)
        print(tmp1)
    tmp1.clear()
