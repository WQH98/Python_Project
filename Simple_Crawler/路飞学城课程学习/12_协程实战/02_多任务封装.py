import time
import asyncio


# 异步任务
async def run(url):
    print("协程开始")
    return url


# 回调函数
def call_bask(f):
    print("返回值", f.result())


async def main():
    url_list = ["baidu.com", "taobao.com", "qq.com"]
    tasks = []
    for url in url_list:
        con = run(url)
        # 创建任务
        task = asyncio.ensure_future(con)
        task.add_done_callback(call_bask)
        tasks.append(task)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # 创建消息循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("over")