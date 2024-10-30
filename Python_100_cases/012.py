# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。

# 输出的列表
result = []
# 是不是素数的标志位
num_flag = 0
# 在101~200之间循环
for i in range(101, 201):
    # 在2到本数之间循环
    for j in range(2, i):
        # tmp是这个数去除2到这个数的结果
        tmp = i / j
        # 判断这个数是不是整数
        if tmp.is_integer():
            # 是整数就标志位置一 且结束这个循环
            num_flag = 1
            break
    # j的循环结束后 判断这个数是不是素数 是的话加入列表 不是把标志位指令
    if num_flag == 0:
        result.append(i)
    else:
        num_flag = 0

# 打印这个列表和列表数量
print(result)
print("The total is %d" % len(result), end="\r\n")
