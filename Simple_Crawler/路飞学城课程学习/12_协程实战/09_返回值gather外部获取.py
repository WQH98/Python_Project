import asyncio


async def run(url):
    print("开始协程")
    return url


async def main():
    url_list = ["baidu.com", "taobao.com", "qq.com"]
    tasks = []
    for url in url_list:
        task = asyncio.ensure_future(run(url))
        tasks.append(task)
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    done = loop.run_until_complete(main())
    for i in done:
        print("返回值", i)
