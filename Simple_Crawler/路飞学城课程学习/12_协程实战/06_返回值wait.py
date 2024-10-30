import asyncio


async def run(url):
    print("开始任务", url)
    return url


async def main():
    url_list = ["baidu.com", "taobao.com", "qq.com"]
    tasks = []
    for url in url_list:
        con = run(url)
        task = asyncio.create_task(con)
        tasks.append(task)
    done, spending = await asyncio.wait(tasks)
    for i in done:
        print("返回值", i.result())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

