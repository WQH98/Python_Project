from bs4 import BeautifulSoup
import pandas as pd


with open("../素材/匹配天气.html", "r", encoding="utf-8") as f:
    str_html = f.read()

soup = BeautifulSoup(str_html, "lxml")

addr_list = []
temp_list = []

div_lists = soup.find_all("div", class_="conMidtab2")[0:7]
for div in div_lists:
    tr_lists = div.find_all("tr")[2:]
    for tr in tr_lists:
        addr_lists = tr.find_all("td", width="83", height="23")
        for addr in addr_lists:
            addr_list.append(addr.text.strip())
        temp_lists = tr.find_all("td", width="92")
        for temp in temp_lists:
            temp_list.append(temp.text.strip())


datas = zip(addr_list, temp_list)
df = pd.DataFrame(datas, columns=["城市", "温度"])
df.to_excel("./天气信息.xlsx", index=False)


