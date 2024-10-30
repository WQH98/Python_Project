import asyncio

async def run():
    print('我是run函数')

# 创建了一个协程对象
coroutine = run()
# asyncio.run(coroutine)  # 新版本的

# 创建事件循环
# 老版本的运行
loop = asyncio.get_event_loop()
# print(loop)
loop.run_until_complete(coroutine)
