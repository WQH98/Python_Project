# 题目：字符串日期转换为易读的日期格式。

import time

date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(date)

