# 题目：输出 9*9 乘法口诀表。
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。

# 行的范围是1~9
for i in range(1, 10):
    # 列的范围是1~i
    for j in range(1, i + 1):
        print("%d * %d = %d" % (i, j, i * j), end="\t")
    print("", end="\r\n")
