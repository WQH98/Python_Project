from lxml import etree


with open("./素材/股票.html", 'r', encoding="utf-8") as f:
    f = f.read()


tree = etree.HTML(f)

trs = tree.xpath('//tbody[@class="tbody_right" and @id="datalist"]//tr')
for tr in trs:
    print(tr.xpath('.//td/a/text() | .//td/text()'))

