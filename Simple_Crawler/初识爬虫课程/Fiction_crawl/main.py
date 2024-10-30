"""
批量爬取全本小说
思路：
    1 爬取目录页 得到所有章的链接地址
    比如 89文学：《圣武星辰》  http://www.89wx.cc/41/41060/
    2 依次爬取每章的小说正文
    比如 第二章 好强大 http://www.89wx.cc/41/41060/14535930.html
"""
import requests
from bs4 import BeautifulSoup



def get_novel_chapters():
    """获取所有小说章节的链接"""
    root_url = "http://www.89wx.cc/41/41060/"
    r = requests.get(root_url)
    r.encoding = "gbk"
    soup = BeautifulSoup(r.text, "html.parser")

    data = []
    for dd in soup.find_all("dd"):
        link = dd.find("a")
        if not link:
            continue
        data.append(("http://www.89wx.cc%s" % link['href'], link.get_text()))
    return data


def get_chapter_content(url):
    r = requests.get(url)
    r.encoding = "gbk"
    suop = BeautifulSoup(r.text, "html.parser")
    return suop.find("div", id='content').get_text()


novel_chapters = get_novel_chapters()
total_cnt = len(novel_chapters)
idx = 0
for chapter in novel_chapters:
    idx += 1
    print(idx, total_cnt)
    url, title = chapter
    with open("%s.txt" % title, "w+", encoding="utf-8") as fout:
        fout.write(get_chapter_content(url))
