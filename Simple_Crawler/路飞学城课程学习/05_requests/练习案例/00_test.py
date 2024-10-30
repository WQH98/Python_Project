import requests
from lxml import etree

url = 'https://movie.douban.com/review/best/?start=0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'
}

res = requests.get(url, headers=headers)

content = res.content.decode()
tree = etree.HTML(content)
divs = tree.xpath('//div[@class="review-list chart "]/div')
for div in divs:
    # img = div.xpath('.//img/@src')[0]
    # title = div.xpath('.//div[@class="main-bd"]/h2/a/text()')[0]
    # name = div.xpath('.//img/@alt')[0]
    # review_url = div.xpath('.//div[@class="main-bd"]/h2/a/@href')[0]
    # review_content = requests.get(review_url, headers=headers).content.decode()
    # review_tree = etree.HTML(review_content)
    # review = review_tree.xpath('//div[@class="review-content clearfix"]/p/text()')
    # review = ' '.join(review)

    subject_url = div.xpath('.//a[@class="subject-img"]/@href')[0]
    subject_content = requests.get(subject_url, headers=headers).content.decode()
    subject_tree = etree.HTML(subject_content)
    subject = subject_tree.xpath('//span[@property="v:summary"]//text()')
    subject = ' '.join(subject).strip()
    print(subject)

