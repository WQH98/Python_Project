import scrapy


class LotterySpider(scrapy.Spider):
    name = "lottery"
    allowed_domains = ["sina.com.cn"]
    start_urls = ["https://view.lottery.sina.com.cn/lotto/pc_zst/index?lottoType=ssq&actionType=chzs&type=50&dpc=1"]

    def parse(self, resp, **key):
        trs = resp.xpath('//tbody[@id="cpdata"]/tr')
        for tr in trs:
            issue = tr.xpath('./td[1]/text()').extract_first()
            red = tr.xpath('./td[@class="chartball01" or @class="chartball20"]/text()').extract()
            blue = tr.xpath('./td[@class="chartball02"]/text()').extract_first()
            yield {
                'issue': issue,
                'red': red,
                'blue': blue
            }
