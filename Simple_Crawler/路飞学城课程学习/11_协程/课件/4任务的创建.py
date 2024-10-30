import asyncio

async def run(i):
    print('我是协程开始', i)
    print('我是协程结束', i)



c = run(1)
# 创建任务
task = asyncio.ensure_future(c)
loop = asyncio.get_event_loop()
# 将任务放到事件循环中
loop.run_until_complete(task)