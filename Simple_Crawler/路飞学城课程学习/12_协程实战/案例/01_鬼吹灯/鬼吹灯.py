import asyncio
import os
import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup


def get_html_source(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    with open("./鬼吹灯.html", 'w', encoding='utf-8') as f:
        f.write(response.text)
    return response.text


def get_book_list_url(html):
    book_list = []
    soup = BeautifulSoup(html, 'html.parser')
    div_list = soup.find_all("div", class_="mulu-list quanji")
    for div in div_list:
        a_list = div.find_all("a")
        for a in a_list:
            chapter_link = a['href']
            book_list.append(chapter_link)
    return book_list


async def download_one_chapter(url, signal):
    for i in range(10):
        try:
            async with signal:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        page_source = await response.text()
                        soup = BeautifulSoup(page_source, 'html.parser')
                        book_name = soup.find('div', class_="crumb").find_all('a')[-1].text
                        chapter_name = soup.find('div', class_="content book-content").find('h1').text
                        chapter_name= chapter_name.replace(' : ', '_')
                        book_path = f'{path}/{book_name}'
                        if not os.path.exists(book_path):
                            os.makedirs(book_path)
                        contexts = soup.find('div', class_="neirong").find_all('p')
                        book_txt = ""
                        for context in contexts:
                            book_txt += context.text + '\n'
                        async with aiofiles.open(f'{book_path}/{chapter_name}.txt', 'w', encoding='utf-8') as f:
                            await f.write(book_txt)
                        print(f"{book_name}/{chapter_name}  下载完毕!")
                        return ""
        except Exception as e:
            print(e)
            print("下载失败 重新下载")
    return url


async def download_all_chapter(url_list):
    tasks = []
    semaphore = asyncio.Semaphore(10)
    for url in url_list:
        con = download_one_chapter(url, semaphore)
        task = asyncio.create_task(con)
        tasks.append(task)
    await asyncio.wait(tasks)
    # await asyncio.gather(*tasks)


if __name__ == '__main__':
    url = 'https://www.51shucheng.net/daomu/guichuideng'
    path = './鬼吹灯'
    if not os.path.exists(path):
        print('未找到下载文件夹 现在开始创建')
        os.mkdir(path)
        print('创建成功')
    # source = get_html_source(url)
    with open("鬼吹灯.html", 'r', encoding='utf-8') as f:
        source = f.read()
    book_list = get_book_list_url(source)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(download_all_chapter(book_list[0:3]))
    # python版本高 所以可以直接使用run
    asyncio.run(download_all_chapter(book_list))

