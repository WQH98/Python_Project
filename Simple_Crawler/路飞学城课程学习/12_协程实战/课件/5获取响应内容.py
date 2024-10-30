import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        # params = {'name': 'lucky', 'name': 'zhangsan'}
        params = [('name', 'lucky'), ('name', 'zhangsan')]
        async with session.get(url='http://httpbin.org/get', params=params) as resp:
            print(resp.status)  # 打印状态码
            # text = await resp.text()  # 获取请求返回的文本
            # text = await resp.text(encoding='UTF-8')  # 获取请求返回的文本
            # print(text)
            # json = await resp.json()  # 获取json数据
            # print(json)
            data = await resp.read()  # 返回bytes
            print(data)

asyncio.run(main())