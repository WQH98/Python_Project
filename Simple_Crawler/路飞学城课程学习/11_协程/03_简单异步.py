import time
import asyncio


async def run():
    print("run start")
    # 这个位置的asyncio.sleep()  用于协程对象中的阻塞等待
    await asyncio.sleep(2)
    print("run end")


if __name__ == '__main__':
    con = run()
    # 直接调用
    # asyncio.run(con)

    loop = asyncio.new_event_loop()
    loop.run_until_complete(con)

