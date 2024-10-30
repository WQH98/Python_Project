import redis
import requests
import time
from lxml import etree

pool = redis.ConnectionPool(password='admin', decode_responses=True)

r = redis.StrictRedis(connection_pool=pool)

url = 'https://www.btwuji.com/html/gndy/dyzz/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
}
res = requests.get(url, headers=headers)
con = res.content.decode("GBK")
tree = etree.HTML(con)
# 匹配标题
titles = tree.xpath('//div[@class="co_content8"]//table//a/text()')
# 匹配简介
infos = tree.xpath('//div[@class="co_content8"]//table//td[@colspan="2"]/text()')

r.rpush('dytt', ''.join(titles) + '========>' + ''.join(infos))

time.sleep(5)

print(r.lrange('dytt', 0, -1))

r.close()

