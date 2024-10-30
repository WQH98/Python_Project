# 题目：时间函数举例2。

import time

if __name__ == "__main__":
    start = time.time()
    for i in range(10000):
        print(i)
    end = time.time()
    print(end - start)
