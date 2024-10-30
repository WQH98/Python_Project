import asyncio
import random


async def run(i):
    print('协程开始', i)
    await asyncio.sleep(random.randint(1, 5))
    print('协程结束', i)
    return i

async def main():
    tasks = []  # 装当前task任务
    for i in range(1, 5):
        task = asyncio.create_task(run(i))
        tasks.append(task)
    return await asyncio.wait(tasks)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # done, pending = loop.run_until_complete(main())
    done, pending = asyncio.run(main())
    # 循环以及完成任务的协程 获取返回值
    for d in done:
        print('返回值', d.result())