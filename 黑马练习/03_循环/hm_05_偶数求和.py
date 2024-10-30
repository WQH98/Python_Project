# 计算0-100之间所有 偶数 的累计求和结果
"""
i = 0
sum_ = 0
while i <= 100:
    if i % 2 != 0:
        i += 1
        continue
    sum_ += i
    i += 1
print("0 - 100求偶数和为%d" % sum_)
"""

i = 0
sum_ = 0

while i <= 100:
    if i % 2 == 0:
        sum_ += i
    i += 1
print("0 - 100求偶数和为%d" % sum_)
