from typing import Iterable

import scrapy
from scrapy import Request


class BookClassificationSpider(scrapy.Spider):
    name = "book_classification"
    allowed_domains = ["17k.com"]
    start_urls = ["https://www.17k.com/all/book/2_0_0_0_0_0_0_0_1.html"]

    def start_requests(self):
        cookies = 'GUID=a019343a-f892-44a3-8cc5-58977a497d50; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F98%252F90%252F96139098.jpg-88x88%253Fv%253D1650527904000%26id%3D96139098%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BqYx51ZhI1%26e%3D1728561749%26s%3D290e10d1a5e07755; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2296139098%22%2C%22%24device_id%22%3A%2218ecd60b5dc74e-0dd0d9ab62dea6-4c657b58-2073600-18ecd60b5ddf28%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22cn.bing.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22a019343a-f892-44a3-8cc5-58977a497d50%22%7D; acw_tc=2760829b17155672404047001e5eccbc4c6561340bfeaf1b745a517152a244; acw_sc__v2=66417a88cfa9e79092f20b5c39aae5affccdd4dd'
        cookies_dic = {}
        cookies_items = cookies.split(';')
        for cookies_item in cookies_items:
            cookies_item = cookies_item.strip()
            k, v = cookies_item.split('=', 1)
            cookies_dic[k] = v
        yield Request(self.start_urls[0], cookies=cookies_dic, callback=self.parse)

    def parse(self, resp, **kwargs):
        # print(resp.text)
        trs = resp.xpath('//table/tbody/tr')
        for tr in trs:
            book_name = tr.xpath('./td[@class="td3"]/span/a[@class="jt"]/text()').extract_first()
            print(book_name)
        urls = resp.xpath('//div[@class="page"]//a/@href').extract()
        for url in urls:
            if url.startswith('java'):
                continue
            url = 'https://www.17k.com' + url
            yield Request(url, callback=self.parse)

