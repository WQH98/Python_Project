from bs4 import BeautifulSoup

# f = open("./素材/豆瓣新书速递.html", "r", encoding="utf-8")
# html_str = f.read()
# f.close()

# 实例化
soup = BeautifulSoup(open("./素材/豆瓣新书速递.html", "r", encoding="utf-8"), "lxml")

# print(soup)

# 获取div标签
# print(soup.div)
# 获取标签的属性
# print(soup.div.attrs)
# {'id': 'db-global-nav', 'class': ['global-nav']}
# print(soup.div.attrs["id"])
# db-global-nav

# 获取文本内容
# print(soup.title)
# print(str(soup.title.string).strip())

# find方法 只拿到一条
# print(soup.find("div"))   # 等同于soup.div
# print(soup.find("div", attrs={'id': 'db-global-nav'}))   # 等同于soup.div 并且id属性值为db-global-nav
# print(soup.find("div", id="db-global-nav"))

# 小练习 获取img的src
# print(soup.find("img", align="left")["src"])
# print(soup.find("img", align="left").attrs["src"])

# 获取文本内容
"""
    find.string 返回第一个文本 如果标签里面还有标签的话 返回None
    find.text   返回当前标签里的所有的文本内容
    find.get_text    等同于上方
    find.strings     返回一个生成器 使用next或list方法可以看到所有的文本 匹配所有 包含空白文本
    find.stripped_strings  返回一个生成器 使用next或list方法可以看到所有的文本 匹配所有 去除空白文本
"""
print(soup.find_all("a", class_="fleft"))
