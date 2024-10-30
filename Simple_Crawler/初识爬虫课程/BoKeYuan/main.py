"""
爬取博客园博客
"""
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.cnblogs.com/AggSite/AggSitePostList"

headers = {
    "Content-Type": "application/json; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.36",
}


def craw_page(page_index):
    data = {
        "CategoryType": "SiteHome",
        "ParentCategoryId": 0,
        "CategoryId": 808,
        "PageIndex": page_index,
        "TotalPostCount": 4000,
        "ItemListActionName": "AggSitePostList"
    }
    # 在请求时 一直请求不通 可以看一下浏览器中 网络->发起程序 是不是json的程序
    # 异步加载的代码
    # 可以把整个headers全部加进来 一个一个测试
    resp = requests.post(url, headers=headers, data=json.dumps(data))
    return resp.text


def parse_data(html):
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.find_all("article", class_="post-item")
    datas = []
    for article in articles:
        link = article.find("a", class_="post-item-title")
        title = link.get_text()
        href = link["href"]
        author = article.find("a", class_="post-item-author").get_text()
        icon_digg = 0
        icon_comment = 0
        icon_views = 0
        for a in article.find_all("a"):
            if "icon_digg" in str(a):
                icon_digg = a.find("span").get_text()
            if "icon_comment" in str(a):
                icon_comment = a.find("span").get_text()
            if "icon_views" in str(a):
                icon_views = a.find("span").get_text()

        datas.append([title, href, author, icon_digg, icon_comment, icon_views])
    return datas


if __name__ == "__main__":
    all_datas = []
    for page in range(20):
        print("正在爬取：", page)
        html = craw_page(page)
        datas = parse_data(html)
        all_datas.extend(datas)

    df = pd.DataFrame(all_datas, columns=["title", "href", "author", "icon_digg", "icon_comment", "icon_views"])
    df.to_excel("博客园200页文章信息.xlsx", index=False)

