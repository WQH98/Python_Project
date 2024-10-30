import asyncio


async def run(url):
    print("start run", url)
    await asyncio.sleep(2)
    print("over run")
    return url


def call_back(future):
    print(future)
    print("call back", future.result())


if __name__ == '__main__':
    con = run("baidu")
    # 创建任务
    task = asyncio.ensure_future(con)
    # 添加回调操作 获取返回值
    task.add_done_callback(call_back)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task)

