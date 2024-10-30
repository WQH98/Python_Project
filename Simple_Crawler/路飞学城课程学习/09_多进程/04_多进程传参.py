import time
from multiprocessing import Process


def run1(num, name):
    for i in range(num):
        print(f"运行{name}函数")
        # 当前代码是单进程的 会在这里阻塞
        time.sleep(1)


if __name__ == '__main__':
    # 如果给的参数只有一个 那么参数后面要加,
    # 不加逗号给的是整形 给了逗号加的是元组
    # 此处也可以用列表 比如Process(target=run1, args=([2])).start()
    # 但是元组的效率比列表高
    Process(target=run1, args=(2, "run1")).start()
