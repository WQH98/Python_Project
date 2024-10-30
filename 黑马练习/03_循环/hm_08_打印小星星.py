# 在控制台连续输出五行 * ，每一行星号的数量依次递增
# 使用循环打印
"""
i = 1
while i <= 5:
    print("*" * i)
    i += 1
"""

# 使用循环嵌套打印
i = 1
j = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("")
    i += 1
