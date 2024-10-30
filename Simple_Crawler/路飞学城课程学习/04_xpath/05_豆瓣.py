from lxml import etree

with open('./素材/豆瓣.html', 'r', encoding='utf-8') as f:
    f = f.read()

tree = etree.HTML(f)

detail_frames = tree.xpath('//div[@class="grid-12-12 clearfix"]//ul//li')

datas = []

for detail_frame in detail_frames:
    titles = detail_frame.xpath('./div/h2/a/text()')
    details = detail_frame.xpath('./div/p[3]/text()')
    img = detail_frame.xpath('./a/img/@src')
    datas.append([titles, details, img])


for data in datas:
    print(data)

