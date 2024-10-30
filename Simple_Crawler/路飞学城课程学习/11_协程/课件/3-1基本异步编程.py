import asyncio

async def run():
    print('我是run函数')

# 创建了一个协程对象
coroutine = run()
# print(coroutine)
asyncio.run(coroutine)