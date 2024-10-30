"""
爬取图片 并且下载图片
url: https://pic.netbian.com/4kmeinv/

爬取网页requests
解析网页BeautySoup
"""
import os.path
import requests
from bs4 import BeautifulSoup


def craw_html(url):
    # 获取网页的源代码

    r = requests.get(url)
    r.encoding = "gbk"
    html = r.text
    return html


def parse_and_download(html):
    # 解析图片的地址
    soup = BeautifulSoup(html, "html.parser")
    imgs = soup.find_all("img")
    for img in imgs:
        src = img["src"]
        if "/uploads/" not in src:
            continue
        src = f"https://pic.netbian.com{src}"
        print(src)
        # 首先得到图片的本地文件地址
        filename = os.path.basename(src)
        with open(f"photos/{filename}", "wb") as f:
            r_img = requests.get(src)
            f.write(r_img.content)


urls = ["https://pic.netbian.com/4kmeinv/"] + [
    f"https://pic.netbian.com/4kmeinv/index_{i}.html"
    for i in range(2, 11)
]

for url in urls:
    print("####正在爬取：", url)
    html = craw_html(url)
    parse_and_download(html)
