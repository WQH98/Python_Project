# 1、使用requests爬取网页
# 2、使用BeautifulSoup实现数据解析
# 3、借助pandas将数据写出到Excel

import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import pprint

# 构造分页数字列表
page_indexs = range(0, 250, 25)
list(page_indexs)


def download_all_htmls():
    """
    下载所有列表页面的HTML 用于后续的分析
    """
    htmls_list = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    for idx in page_indexs:
        url = f"https://movie.douban.com/top250?start={idx}&filter="
        print("craw html:", url)
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            raise Exception("error")
        htmls_list.append(r.text)

    return htmls_list


def parse_single_html(html):
    """
    解析单个HEML 得到数据
    :param html:
    :return: list({"link", "title", [label]})
    """
    soup = BeautifulSoup(html, 'html.parser')
    article_items = (
        soup.find("div", class_="article")
        .find("ol", class_="grid_view")
        .find_all("div", class_="item")
    )
    datas = []
    for article_item in article_items:
        rank = article_item.find("div", class_="pic").find("em").get_text()
        info = article_item.find("div", class_="info")
        title = info.find("div", class_="hd").find("span", class_="title").get_text()
        stars = (
            info.find("div", class_="bd")
            .find("div", class_="star")
            .find_all("span")
        )
        rating_star = stars[0]["class"][0]
        rating_num = stars[1].get_text()
        comments = stars[3].get_text()

        datas.append({
                "rank": rank,
                "title": title,
                "rating_star": rating_star.replace("rating", "").replace("-t", ""),
                "rating_num": rating_num,
                "comments": comments.replace("人评价", "")
            })

    return datas


if __name__ == "__main__":
    htmls = download_all_htmls()
    all_datas = []
    for html in htmls:
        all_datas.extend(parse_single_html(html))

    print(len(all_datas))
    pprint.pprint(all_datas)
    df = pd.DataFrame(all_datas)

    df.to_excel("豆瓣电影TOP250.xlsx")
