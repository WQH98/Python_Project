from bs4 import BeautifulSoup
import pandas as pd

f = open("../素材/广州二手房.html", "r", encoding="utf-8")
html_str = f.read()
f.close()

soup = BeautifulSoup(html_str, "lxml")

div_list = soup.find_all("div", class_="house-item house-itemB clearfix")

datas = []

for div in div_list:
    title = div.find("h4", class_="house-title").text.strip()
    name1 = div.find("p", class_="house-name").find("a").text
    name2 = div.find("p", class_="house-name").find_all("span")[1].text
    name3 = div.find("p", class_="house-name").find_all("span")[-2].text
    txts = div.find("p", class_="house-txt")
    txt1 = ""
    for txt in txts.find_all("span"):
        txt1 += txt.text
        txt1 += " "

    txts = div.find_all("p", class_="house-txt")[-1]
    txt2 = txts.text.strip()

    prices = div.find("p", class_="price-nub cRed")
    prices = prices.text.strip().replace("\n", "")

    price_txt = div.find("p", class_="price-txt")
    price_txt = price_txt.text.strip().replace("\n", "").replace("                    ", "")

    price_txtB = div.find("p", class_="price-txtB")
    price_txtB = price_txtB.text.strip()
    datas.append([title, name1, name2, name3, txt1, txt2, prices, price_txt, price_txtB])


df = pd.DataFrame(datas, columns=["标题", "详细地址", "户型", "平方数", "详情", "地址", "价格", "单价", "小区均价"])
df.to_excel("二手房信息.xlsx", index=False)








