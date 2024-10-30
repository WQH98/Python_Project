import time
import asyncio


async def run(url):
    print(f'向{url}抓取数据开始')
    await asyncio.sleep(2)
    print(f'向{url}抓取数据结束')


if __name__ == '__main__':
    t1 = time.time()
    task_list = []
    # 开启了3个任务
    for i in range(3):
        c = run(i)
        # 创建任务
        task = asyncio.ensure_future(c)
        task_list.append(task)
    # print(asyncio.wait(task_list))
    # exit()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))
    print(time.time()-t1)