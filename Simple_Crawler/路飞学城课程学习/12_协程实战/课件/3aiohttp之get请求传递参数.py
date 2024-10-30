import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        params = {'name': 'lucky', 'age': 18}
        async with session.get(url='http://httpbin.org/get', params=params) as resp:
            print(resp.status)  # 打印状态码
            text = await resp.text()  # 获取请求返回的文本
            print(text)



asyncio.run(main())