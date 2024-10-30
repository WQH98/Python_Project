# 无忧考网爬取文章
import time

import requests
from bs4 import BeautifulSoup
import openpyxl
import pandas as pd
import random

root_url = "https://list.51test.net/w/?nclassid=206&key=&search_key=%BB%FD%BC%AB&search_key2=&page=1"

data = {
    "nclassid": "206",
    "key": "",
    "search_key": "%BB%FD%BC%AB",
    "search_key2": "",
    "page": "1",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46",
    "Referer": "https://www.51test.net/",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-User": "?1",
    "Sec - Ch - Ua - Mobile": "?0",
    "Sec - Ch - Ua - Platform": '''"Windows"''',
    "Sec - Fetch - Dest": "document",
    "Sec - Fetch - Mode": "navigate",
    "Sec - Fetch - Site": "none",
    "Sec - Ch - Ua": '''"Chromium";v = "118", "Microsoft Edge";v = "118", "Not=A?Brand";v = "99"''',
    "Dnt": "1",
    "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.7",
    "Accept - Encoding": "gzip, deflate, br",
    "Accept - Language": "zh - CN, zh;q = 0.9, en;q = 0.8",
    "Cache - Control": "max - age = 0"
}


def url_get():
    links = []
    titles = []
    r = requests.get(root_url, headers=headers, data=data)
    # r = requests.get(root_url, headers=headers)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text, "html.parser")
    # 取出总共有多少页 这样可以写一个循环 有一个循环次数
    all_page = soup.find("div", class_="list_content_next").find("strong").text.split('/')[1]
    for i in range(1, int(all_page) + 1):
        url = f"https://list.51test.net/w/?nclassid=206&key=&search_key=%BB%FD%BC%AB&search_key2=&page={i}"
        r = requests.get(url, headers=headers)
        r.encoding = 'gb2312'
        # 现在做的是把当前页的每个网址先搞出来
        soup = BeautifulSoup(r.text, "html.parser")
        lis = soup.find_all("li")
        for li in lis:
            if "class" in str(li):
                continue
            li_url = li.find('a')["href"]
            title = li.find('a').text
            links.append(li_url)
            titles.append(title)
        print(f"正在爬取第{i}页的目录")
    print("目录爬取完成")
    return links, titles


# 解析单个目录的内容
def parse_single_html(link):
    try:
        r = requests.get(link, headers=headers)
    except:
        time.sleep(30)
        print("连接异常 30秒后重新连接")
        r = requests.get(link, headers=headers)
    r.encoding = "gb2312"
    soup = BeautifulSoup(r.text, "html.parser")
    message = (soup.find("div", class_="container")
               .find("div", class_="main-bg")
               .find("div", class_="content-fl")
               .find("div", class_="content-txt")
               .text)
    return message


# 打印出所有的url和标题
if __name__ == "__main__":
    links, titles = url_get()
    directory = []
    for i in range(len(links)):
        directory.append({
            "link": links[i],
            "title": titles[i],
        })
    # 将目录输出到一个EXCEL
    df = pd.DataFrame(directory)
    df.to_excel("积极分子思想汇报目录.xlsx")
    datas = []
    for i in range(len(links)):
        data = parse_single_html(links[i]).split("\r\n\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\n\n\n\n\n\n")[0]
        data = data.replace("\u3000\u3000", "\n\t")
        datas.append(data)
        s = random.randint(5, 10)
        time.sleep(s)
        with open(f"output/{titles[i]}.txt", "w", encoding="utf-8") as file:
            file.write(data)
        print(f"共{len(links)}篇 爬取第{i}篇完成 随机延时{s}秒")
