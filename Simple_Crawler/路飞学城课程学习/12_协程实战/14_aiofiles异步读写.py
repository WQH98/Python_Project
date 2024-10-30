import asyncio
import aiofiles


async def main():
    async with aiofiles.open('01_多任务(ensure_future).py', 'r', encoding='utf-8') as f:
        return await f.readlines()


print(asyncio.run(main()))
