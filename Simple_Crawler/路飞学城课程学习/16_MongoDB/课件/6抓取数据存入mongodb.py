import requests
from lxml import etree
from pymongo import MongoClient
conn = MongoClient('localhost')
db = conn.test  # 选择数据库
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
url = 'https://www.3dst.cn/t/lizhigushi/'
res = requests.get(url, headers=headers)
data = res.content.decode()
print(data)
tree = etree.HTML(data)
#获取所以超链接的url
a_list = tree.xpath('/html/body/main/div[1]/div[2]/ul/li/a/@href')
# print(a_list)
for a in a_list:
    res = requests.get(a, headers=headers)
    tree = etree.HTML(res.content.decode())
    # 标题
    title = tree.xpath('/html/body/main/div/article/h1/text()')[0]
    # 作者
    author = tree.xpath('/html/body/main/div/article/div[1]/span[3]/text()')[0]
    # 文章
    article = tree.xpath('//div[@class="content"]//text()')
    article = ''.join(article).replace('"', '')  # 处理文章中的双引号 防止和外层的引号发生冲突 这样数据就会写入失败
    # 插入数据库
    db.article.insert_one({'title': f"{title}", 'author': f"{author}", 'article': f"{article}"})
conn.close()
