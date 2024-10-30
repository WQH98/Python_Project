from lxml import etree

with open('./素材/大学排名.html', 'r', encoding='utf-8') as f:
    f = f.read()


tree = etree.HTML(f)

res = tree.xpath('//table[@class="sticky-enabled tableheader-processed sticky-table"]/tbody//tr')
# print(res)
for tr in res:
    print(tr.xpath('./td//text()'))


