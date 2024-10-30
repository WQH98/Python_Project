# 题目：暂停一秒输出，并格式化当前时间。
# 程序分析：无。

import time

# strftime()函数用于格式化时间 返回以可读字符串表示的当地时间 格式由参数format决定
# time.strftime(format[, t])
# format -- 格式字符串。
# t -- 可选的参数 t 是一个 struct_time 对象。
print(time.strftime("%Y-%m-%d %H:%M:%S"))

time.sleep(1)

print(time.strftime("%Y-%m-%d %H:%M:%S"))
