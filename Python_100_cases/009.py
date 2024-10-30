# 题目：暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。

import time
# 定义等会儿要输出的元组
dst = {1: 'a',
       2: 'b',
       3: 'c',
       4: 'd',
       5: 'e'}
# items()函数作用 以列表返回可遍历的（键 值）元组数据
for key, value in dst.items():
    print(key, value)
    # 延时1秒
    time.sleep(1)
