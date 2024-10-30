from bs4 import BeautifulSoup

with open("../素材/三国演义.html", "r", encoding="utf-8") as f:
    html_str = f.read()

soup = BeautifulSoup(html_str, "lxml")
title = soup.find("div", class_="card bookmark-list").find("h1").text
print(title)
datas = title + "\n"
period = soup.find("div", class_="card bookmark-list").find("div").find_all("p")[0].text
print(period)
datas += period
datas += "\n"
author = soup.find("div", class_="card bookmark-list").find("div").find_all("p")[1].text
print(author)
datas += author
datas += "\n"
catalogs = soup.find("div", class_="book-mulu").find("ul").find_all("li")
for catalog in catalogs:
    print(catalog.find("a").string)
    datas += catalog.find("a").string
    datas += "\n"

with open("./三国演义.txt", "w", encoding="utf-8") as f:
    f.write(datas)
