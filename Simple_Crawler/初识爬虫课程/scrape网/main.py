import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

max_retries = 10       # 最大重试次数
retry_delay = 5        # 最大延迟时间


headers = {
    "User - Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Upgrade-Insecure-Requests": "1",
    "Referer": "https://ssr1.scrape.center/page/1",
    "Host": "ssr1.scrape.center",
}


def get_url():
    r = ""
    urls = []
    # 构建url
    for i in range(1, 11):
        url = f"https://ssr1.scrape.center/page/{i}"
        retries = 0
        while retries < max_retries:
            try:
                r = requests.get(url, headers=headers)
                break  # 请求成功，跳出重试循环
            except requests.exceptions.ConnectionError as e:
                retries += 1
                print(f"连接错误，正在进行第{retries}次重试...")
                time.sleep(retry_delay)  # 等待一段时间后重试
        else:
            print("达到最大请求次数 连接失败 直接退出")
            sys.exit(-1)
        soup = BeautifulSoup(r.text, "html.parser")
        hrefs = soup.find_all("div", class_="el-card item m-t is-hover-shadow")
        for href in hrefs:
            link = href.find("a").get("href")
            link = f"https://ssr1.scrape.center{link}"
            urls.append(link)
        print(f"完成第{i}页的爬取")
        time.sleep(2)
    return urls


def analysis_url(all_url):
    r = ""
    i = 0
    datas = []
    for url in all_url:
        i += 1
        print(f"开始爬取第{i}个链接")
        retries = 0
        while retries < max_retries:
            try:
                r = requests.get(url, headers=headers)
                break
            except requests.exceptions.ChunkedEncodingError as e:
                retries += 1
                print(f"连接错误，正在进行第{retries}次重试...")
                time.sleep(retry_delay)  # 等待一段时间后重试
        else:
            print("达到最大请求次数 连接失败 直接退出")
            sys.exit(-1)
        categories = []
        soup = BeautifulSoup(r.text, "html.parser")
        movie_name = soup.find("h2", class_="m-b-sm").text
        tags = soup.find("div", class_="categories").find_all("button")
        for tag in tags:
            category = " ".join(tag.stripped_strings)
            categories.append(category)
        movie_result = ",".join(categories)
        temps = soup.find_all("div", class_="m-v-sm info")
        movie_local = temps[0].get_text(strip=True).split("/")[0]
        movie_time = temps[0].get_text(strip=True).split("/")[1]
        movie_up_time = temps[1].get_text(strip=True)
        movie_synopsis = soup.find("div", class_="drama").find("p").text.strip()
        movie_director = soup.find("p", class_="name text-center m-b-none m-t-xs").text
        movie_score = soup.find("p", class_="score m-t-md m-b-n-sm").text.strip()
        datas.append([movie_name, movie_result, movie_local, movie_time, movie_up_time, movie_synopsis, movie_director, movie_score])
    return datas


if __name__ == "__main__":
    urls = get_url()
    datas = analysis_url(urls)
    df = pd.DataFrame(datas, columns=["电影名字", "电影标签", "上映地点", "电影时间", "上映时间", "剧情简介", "导演", "评分"])
    df.to_excel("movie.xlsx", index=False)