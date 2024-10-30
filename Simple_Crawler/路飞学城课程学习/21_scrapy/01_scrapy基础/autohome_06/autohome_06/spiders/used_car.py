import scrapy
from scrapy import Request

class UsedCarSpider(scrapy.Spider):
    name = "used_car"
    allowed_domains = ["che168.com"]
    start_urls = ["https://www.che168.com/nlist/beijing/list/?pvareaid=100533"]

    def parse(self, resp, **kwargs):
        # print(resp.text)
        # 找到每一页的详情页的url 然后发送新的请求
        hrefs = resp.xpath('//ul[@class="viewlist_ul"]/li/a/@href').extract()
        hrefs = hrefs[:-1]
        for href in hrefs:
            child_url = resp.urljoin(href)
            # print(child_url)
            # 发送请求到详情页
            yield Request(url=child_url, callback=self.parse_detail)

    def parse_detail(self, resp, **kwargs):
        title = resp.xpath('//h3[@class="car-brand-name"]/text()').extract_first()
        price = resp.xpath('//span[@id="overlayPrice"]/text()').extract_first()
        print(title, '=======>', price)
