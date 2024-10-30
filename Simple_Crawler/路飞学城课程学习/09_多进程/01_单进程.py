import time


def run():
    print("运行run函数")
    # 当前代码是单进程的 会在这里阻塞
    time.sleep(1000)


# 单进程 程序从上往下执行
run()
print("下面的代码")
