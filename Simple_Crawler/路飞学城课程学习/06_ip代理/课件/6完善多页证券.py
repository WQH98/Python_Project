import requests
from lxml import etree
import re
def get_page(url):
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    data = res.text
    tree = etree.HTML(data)
    li_list = tree.xpath('//ul[@class="list-con"]/li')
    for li in li_list:
        print(li.xpath('./span/text()'))

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    url = 'http://www.cs.ecitic.com/newsite/cpzx/jrcpxxgs/zgcp/index.html'
    # 先请求一次  抓到当前总页码数
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    data = res.text
    # 抓取到总页码数
    total_num = int(re.search('var countPage = (?P<page>\d+)//共多少页', data).group('page'))
    # print(total_num)
    # exit()
    '''
    把瑕疵补充完整
    '''
    for i in range(3, 0, -1):
        pageNum = int(input('输入你要抓取的页码数：'))
        # 判断输入的页码是否在规范内
        if pageNum <= 0 or pageNum > total_num:
            print(f'请输入正确的页码,您还有{i-1}次机会')

    for i in range(pageNum):
        url = f'http://www.cs.ecitic.com/newsite/cpzx/jrcpxxgs/zgcp/index_{i}.html'
        if i == 0:
            url = 'http://www.cs.ecitic.com/newsite/cpzx/jrcpxxgs/zgcp/index.html'
        get_page(url)