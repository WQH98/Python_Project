from typing import Any
import redis
import scrapy
from scrapy import signals, Request
from scrapy.crawler import Crawler
from typing_extensions import Self


class NewthreadSpider(scrapy.Spider):
    name = "newthread"
    allowed_domains = ["52pojie.cn"]
    start_urls = ["https://www.52pojie.cn/forum.php?mod=guide&view=newthread"]

    @classmethod
    def from_crawler(cls, crawler: Crawler, *args: Any, **kwargs: Any) -> Self:
        s = cls()
        # s._set_crawler(crawler)
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(s.spider_closed, signal=signals.spider_closed)
        return s

    def parse(self, resp, **kwargs):
        hrefs = resp.xpath('//div[@class="bm_c"]/table/tbody/tr/th/a[1]/@href').extract()
        for href in hrefs:
            href = resp.urljoin(href)
            if self.red.sismember('pojie:hrefs', href):
                print('该链接存在于数据库 不爬', href)
            else:
                yield Request(url=href,
                              callback=self.parse_detail,
                              meta={
                                  'href': href,
                              })

    def parse_detail(self, resp, **kwargs):
        title = resp.xpath('//span[@id="thread_subject"]/text()').extract_first()
        href = resp.meta.get('href')
        print(title, href)
        self.red.sadd('pojie:hrefs', href)

    def spider_opened(self):
        print("spider_opened")
        self.red = redis.Redis(db=2, password='admin')

    def spider_closed(self):
        print("spider_closed")
        self.red.save()
        self.red.close()

