import aiohttp
import asyncio


async def fetch(session, url):
    # 异步请求网址
    async with session.post(url, data="传递数据") as response:
        # 将响应的内容返回
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        source = await fetch(session, url='https://httpbin.org/post')
        print(source)


asyncio.run(main())
