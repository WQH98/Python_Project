# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
# 思路：使用两个循环变量 一个用来表示现在报数到哪了 范围是1-3 另一个变量表示现在是那个变量来报数的

if __name__ == "__main__":
    n = int(input("Please enter the number of people: "))
    num = []
    j = 1
    k = 0
    for i in range(n):
        num.append(i + 1)
    while len(num) != 1:
        if j % 3 == 0:
            j = 0
            del(num[k])
            k -= 1

        j += 1
        k += 1
        if k > (len(num) - 1):
            k = 0
    print(num)
