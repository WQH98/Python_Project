import time
from multiprocessing import Pool


def get_data(url):
    print("子进程开始", url)
    time.sleep(2)
    print("子进程结束", url)


if __name__ == '__main__':
    url = "http://www.baidu.com?page="
    # 传参 开启几个进程 默认参数是CPU的核心数
    pool = Pool(3)
    url_list = []
    for i in range(10):
        new_url = url + str(i)
        url_list.append(new_url)
    pool.map(get_data, url_list)
    # 关闭池子 不再放进程了
    pool.close()
    # 阻塞等待
    pool.join()
    print("主进程结束")

