# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
# 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

# 输出的数组
result = []

# 输入3个数字 并加入数组中
for i in range(3):
    sum_in = int(input("please enter value: "))
    result.append(sum_in)

# 对数组进行排序
result.sort()

# 把数组打印出来
print(result)
