from bs4 import BeautifulSoup
import pandas as pd


f = open("../素材/豆瓣.html", "r", encoding="utf-8")
str_html = f.read()
f.close()

soup = BeautifulSoup(str_html, "lxml")

datas = []

# 获取标题 评分 简介等信息
div_lists = soup.find_all("div", class_="detail-frame")
for div in div_lists:
    title = div.find("h2").find("a").text
    score = div.find("p", class_="rating").find("span", class_="font-small color-lightgray").string.strip()
    brief_introductions = div.find_all("p")[-1].string.strip()
    datas.append([title, score, brief_introductions])


df = pd.DataFrame(datas, columns=["标题", "分数", "简介"])
df.to_excel("豆瓣.xlsx", index=False)


