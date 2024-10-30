import time
import asyncio


async def run(url):
    print(f"开始请求{url}的数据")
    await asyncio.sleep(2)
    print(f"结束请求{url}的数据")
    data = url + "的抓取数据"
    return data


# 接收返回值
def call_bask(f):
    print(f.result())


if __name__ == '__main__':
    t1 = time.time()
    # 创建任务
    loop = asyncio.get_event_loop()
    url_list = ["baidu.com", "taobao.com", "qq.com"]
    # 包含多个task任务的对象
    tasks = []
    for url in url_list:
        con = run(url)
        # 开启消息循环
        task = asyncio.ensure_future(con)
        # 添加回调函数
        task.add_done_callback(call_bask)
        tasks.append(task)
    # 任务函数注册到消息循环上
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - t1)
