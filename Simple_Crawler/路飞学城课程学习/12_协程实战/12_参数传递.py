import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        params = {
            'name': 'tom',
            'age': 18
        }
        async with session.get('https://httpbin.org/get', params=params) as response:
            data = await response.text()
            print(data)
            return data


asyncio.run(main())
