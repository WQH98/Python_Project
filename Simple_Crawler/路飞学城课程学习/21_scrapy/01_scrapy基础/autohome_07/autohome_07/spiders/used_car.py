import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor


class UsedCarSpider(scrapy.Spider):
    name = "used_car"
    allowed_domains = ["che168.com"]
    start_urls = ["https://www.che168.com/nlist/beijing/list/?pvareaid=100533"]

    def parse(self, resp, **kwargs):
        # 1、获取每个详情页的url 访问这个url
        # scrapy有个链接提取器能帮我们自动的提取链接
        # 创建一个提取器对象
        lkor1 = LinkExtractor(restrict_xpaths=('//ul[@class="viewlist_ul"]/li/a', ))
        # 让提取器去提取你需要的链接
        links = lkor1.extract_links(resp)
        # for link in links:
            # 当你打印对象的时候 实际上再执行他的__repr__或者__str__
            # print(link)
            # yield Request(url=link.url, callback=self.parse_detail)
        # 2、获取到分页的url 访问这个url
        lkor2 = LinkExtractor(restrict_xpaths=('.//div[@id="listpagination"]/a', ))
        pg_links = lkor2.extract_links(resp)
        for pg_link in pg_links:
            print(pg_link)


    def parse_detail(self, resp, **kwargs):
        pass
