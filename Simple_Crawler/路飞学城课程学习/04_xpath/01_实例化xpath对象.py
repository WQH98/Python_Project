from lxml import etree


# 本地HTML文件 这样可能会出现编码错误的问题
# parser = etree.HTMLParser(encoding="utf-8")
# tree = etree.parse("./素材/豆瓣.html", parser=parser)
# print(tree)

# 网络HTML字符串或者本地的HTML文件都可以（建议）
with open("./素材/豆瓣.html", "r", encoding="utf-8") as f:
    html_str = f.read()

tree = etree.HTML(html_str)
print(tree)
