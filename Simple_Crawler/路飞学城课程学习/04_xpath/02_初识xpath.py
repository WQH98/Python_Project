from lxml import etree

# 实例化tree对象
with open("./素材/豆瓣.html", mode="r", encoding="utf-8") as f:
    str_html = f.read()
tree = etree.HTML(str_html)
# print(tree)
# xpath("语法")

# 想拿到登录和注册的按钮标题
# /html/body/div/div/div/a/
# res = tree.xpath("/html/body/div/div/div/a")
# for re in res:
#     print(re.text)

# 节点对象转换成字符串输出
# print(etree.tostring(res[0], encoding="utf-8").decode("utf-8"))
# print(etree.tostring(res[1], encoding="utf-8").decode("utf-8"))
# print(etree.tostring(res[2], encoding="utf-8").decode("utf-8"))
# 或者使用循环
# for e in res:
#     print(etree.tostring(e, encoding="utf-8").decode("utf-8"))

# 超链接a  获取页面中所有的a  不管a在哪个地方
# res = tree.xpath("//a")
# res = tree.xpath("//img")   # 获取页面中所有的img标签
# for e in res:
#     print(etree.tostring(e, encoding="utf-8").decode("utf-8"))


# res = tree.xpath("/html/body/div/div/div/a/text()")  # 获取a中的文本内容
# res = tree.xpath("//a/text()")  # 获取所有a中的文本内容
# print(res)


# 获取登录注册 不要豆瓣
# 在xpath语法中 获取是从1开始的
# res = tree.xpath('/html/body/div/div/div[1]/a/text()')
# print(res)


# / 和 // 在下一次路径中的使用
# res = tree.xpath('/html/body/div/div/div/a')
# 进行二级匹配
# ./  相当于从当前节点对象继续往下匹配
# 等同于tree.xpath('/html/body/div/div/div[1]/a/text()')
# print(res[0].xpath("./text()"))


# 路径中混合使用/ 和 //
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]')
# for e in res:
#     print(etree.tostring(e, encoding="utf-8").decode("utf-8"))
# 获取虚构类中的所有的li内的文本内容
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li//text()')
# print(res)
# 获取虚构类里的所有li内的img标签
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]//img')
# for e in res:
#     print(etree.tostring(e, encoding="utf-8").decode("utf-8"))
# 获取虚构类里的所有li内的img标签的src属性值
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]//img/@src')
# print(res)


# 数量限制
# 想要第一个li 使用的是xpath语法 也可以用python的列表 切片操作 来替代
# res1 = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li[1]')
# print(etree.tostring(res1[0], encoding="utf-8").decode("utf-8"))
# 使用切片操作
# res1 = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li')[0]
# print(etree.tostring(res1[1], encoding="utf-8").decode("utf-8"))
# 获取最后一个li
# res1 = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li[last()]')
# print(etree.tostring(res1[0], encoding="utf-8").decode("utf-8"))
# 获取倒数第二个li
# res1 = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li[last()-1]')
# print(etree.tostring(res1[0], encoding="utf-8").decode("utf-8"))
# 获取前两个li
# res = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li[position() < 3]')
# print(etree.tostring(res[0], encoding="utf-8").decode("utf-8"))
# print(etree.tostring(res[1], encoding="utf-8").decode("utf-8"))


# 判断
# 获取所有带有class属性的a标签
# res = tree.xpath('//a[@class]')
# 获取所有class属性值"cover"的a标签
# res = tree.xpath('//a[@class="cover"]')
# 获取所有price属性值大于10的a标签
# res = tree.xpath('//a[@price > "10"]')
# for e in res:
#     print(etree.tostring(e, encoding="utf-8").decode("utf-8"))
# 获取所有price属性值大于等于10的a标签
# res = tree.xpath('//a[@price >= "10"]')
# for e in res:
#     print(etree.tostring(e, encoding="utf-8").decode("utf-8"))
# 获取所有price属性值不等于10的a标签
# res = tree.xpath('//a[@price != "10"]')
# for e in res:
#     print(etree.tostring(e, encoding="utf-8").decode("utf-8"))


# 通配符*的使用 一般只有在copy xpath的时候会出现* 自己写的时候很少用
# 获取所有具有price属性的标签(无论什么标签)
# res = tree.xpath('//*[@price]')
# for e in res:
#     print(etree.tostring(e, encoding="utf-8").decode("utf-8"))


# node()
# res = tree.xpath('//node()')
# for e in res:
#     print(etree.tostring(e, encoding="utf-8").decode("utf-8"))


# 匹配class为div1或class为div2的
# res = tree.xpath('//div[@class="div1"] | //div[@class="div2"]')
# and 匹配div标签 其中class值为div1 并且 id值为test1的
# res = tree.xpath('//div[@class="div1" and @id="test1"]/text()')
# print(res)


# 包含
# div标签中 class属性值包含d的节点
# res = tree.xpath('//div[contains(@class, "d")]')
# div标签中 class属性值以d开头的
res = tree.xpath('//div[starts-with(@class, "d")]')
print(res)

