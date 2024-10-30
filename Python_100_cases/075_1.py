# 题目：放松一下，算一道简单的题目。
# Python time strftime() 函数用于格式化时间，返回以可读字符串表示的当地时间，格式由参数 format 决定。
# strftime()方法语法：time.strftime(format[, t])
# format -- 格式字符串。t -- 可选的参数 t 是一个 struct_time 对象。

# Python time localtime() 函数类似gmtime()，作用是格式化时间戳为本地的时间。
# 如果sec参数未输入，则以当前时间为转换标准。 DST (Daylight Savings Time) flag (-1, 0 or 1) 是否是夏令时。
# localtime()方法语法：time.localtime([ sec ])
# sec -- 转换为time.struct_time类型的对象的秒数。

import time

if __name__ == "__main__":
    date = time.strftime("%m-%d", time.localtime())
    if date == "02_14":
        print("is Valentine's Day")
    else:
        print("is not Valentine's Day")
    print(date)
    print("is a test")
