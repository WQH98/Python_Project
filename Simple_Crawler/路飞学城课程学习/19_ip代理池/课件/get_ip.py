'''
抓取ip的文件
'''
import requests
from proxy_redis import ProxyRedis  # ip代理池中处理ip的类
from lxml import etree


# 抓取ip
def get_ip():
    # 实例化处理ip的类
    p_r = ProxyRedis()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Cookie': 'Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1663156133,1663158484; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1663158484'

    }
    # url = 'http://www.66ip.cn/index.html'
    # res = requests.get(url, headers=headers)
    # html = res.content.decode('GBK')  # 解码
    with open('66.html', 'r', encoding='UTF-8') as f:
        html = f.read()
    print(html)
    # 实例化xpath对象
    tree = etree.HTML(html)
    # 匹配到ip和端口 并使用切片去除不要的标题数据
    ip_list = tree.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/tr/td[1]/text()|//*[@id="main"]/div[1]/div[2]/div[1]/table/tr/td[2]/text()')[2:]
    # print(ip)
    # 循环拼接端口和ip
    for i in range(0, len(ip_list), 2):
        # print(ip_list[i] + ':' +ip_list[i+1])
        ip = ip_list[i] + ':' +ip_list[i+1]
        p_r.zset_zadd(ip)  # ip添加到有序集合中


if __name__ == '__main__':
    get_ip()   # 运行测试