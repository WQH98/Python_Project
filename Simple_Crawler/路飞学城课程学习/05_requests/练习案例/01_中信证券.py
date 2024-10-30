import requests
from lxml import etree

url_list = ['http://www.cs.ecitic.com/newsite/cpzx/jrcpxxgs/zgcp/index.html']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
}


def build_url():
    # 共有103页 但是不知道怎么拿js代码 在这里写固定值
    for i in range(1, 103):
        temp = f'http://www.cs.ecitic.com/newsite/cpzx/jrcpxxgs/zgcp/index_{i}.html'
        url_list.append(temp)


def parse_output(url):
    res = requests.get(url, headers=headers)
    content = res.content.decode('utf-8')
    tree = etree.HTML(content)
    lis = tree.xpath('//ul[@class="list-con"]/li')
    for li in lis:
        print(li.xpath('./span/text()'))


if __name__ == "__main__":
    build_url()
    page = int(input('please input page: '))
    if page < 0 or page > 103:
        exit('input err!!! please restart code')
    if page == 0:
        for url in url_list:
            parse_output(url)
    else:
        parse_output(url_list[page - 1])

