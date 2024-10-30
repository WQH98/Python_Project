import time
import asyncio


async def run(url):
    print(f'向{url}抓取数据开始')
    await asyncio.sleep(2)
    print(f'向{url}抓取数据结束')


async def main():
    task_list = []
    # 开启了3个任务
    for i in range(3):
        c = run(i)
        # 创建任务
        task = asyncio.ensure_future(c)
        task_list.append(task)
    await asyncio.wait(task_list)

if __name__ == '__main__':
    t1 = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print(time.time()-t1)