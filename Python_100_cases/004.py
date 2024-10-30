# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

year = int(input("year:"))
month = int(input("month:"))
day = int(input("day:"))

sum_day = 0

# 做一个不是闰年的数组
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 先判断今年是不是闰年
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    run_year = 1
else:
    run_year = 0

# 计算今年在非闰年的情况下过了多少天
for i in range(0, month - 1):
    sum_day += month_day[i]

sum_day += day

# 如果是闰年 且月份大于2 则再加1天
if (month > 2) and (run_year == 1):
    sum_day += 1

# 打印出今年过了多少天
print(sum_day)


