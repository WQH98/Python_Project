import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class UsedCarSpider(CrawlSpider):
    name = "used_car"
    allowed_domains = ["che168.com"]
    start_urls = ["https://www.che168.com/nlist/beijing/list/?pvareaid=100533"]

    # 提取详情页的url
    lk1 = LinkExtractor(restrict_xpaths=('//ul[@class="viewlist_ul"]/li/a', ))
    lk2 = LinkExtractor(restrict_xpaths=('.//div[@id="listpagination"]/a', ))
    # 提取分页的url

    # 配置一些规则
    rules = (
        # parse_item的作用 当整个响应回来之后 先经过链接提取器的提取 拿到详情页的url
        # 然后自动发送请求 这个详情页的url响应回来之后 去执行的callback
        # follow表示你的链接提取器提取的链接 发送请求回来之后 是否需要执行当前所有的规则
        Rule(lk1, callback="parse_item", follow=False),   # 规则1、详情页的逻辑
        Rule(lk2, follow=True),   # 规则2、分页的逻辑
    )

    def parse_item(self, resp, **kwargs):
        print(resp.url)

