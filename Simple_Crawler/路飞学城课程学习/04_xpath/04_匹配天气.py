from lxml import etree

with open('./素材/匹配天气.html', 'r', encoding='utf-8') as f:
    f = f.read()

tree = etree.HTML(f)

tables = tree.xpath('//table[@width="100%"]')
for table in tables:
    trs = table.xpath('./tr')[2:]
    for tr in trs:
        print(tr.xpath('./td//text()'))

