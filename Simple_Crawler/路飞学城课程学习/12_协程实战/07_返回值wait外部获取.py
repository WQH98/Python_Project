import asyncio


async def run(url):
    print("协程开始")
    return url


async def main():
    url_list = ["baidu.com", "taobao.com", "qq.com"]
    tasks = []
    for url in url_list:
        con = run(url)
        task = asyncio.create_task(con)
        tasks.append(task)
    return await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    done, spending = loop.run_until_complete(main())
    for i in done:
        print("返回值", i.result())

