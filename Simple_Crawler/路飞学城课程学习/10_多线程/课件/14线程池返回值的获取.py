from concurrent.futures import ThreadPoolExecutor, as_completed


def run(i):
    print('开始执行子线程', i)
    return i



if __name__ == '__main__':
    pool = ThreadPoolExecutor(3)
    List = [1, 2, 3, 4, 5]
    # all_task = [pool.submit(run, i) for i in List]
    # for i in as_completed(all_task):
    #     print(i.result())  # 获取返回值

    for res in pool.map(run, List):
        print(res)