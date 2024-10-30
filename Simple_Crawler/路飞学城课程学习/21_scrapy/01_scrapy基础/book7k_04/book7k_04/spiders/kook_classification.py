import scrapy
from scrapy import Request


class KookClassificationSpider(scrapy.Spider):
    name = "kook_classification"
    allowed_domains = ["17k.com"]
    start_urls = ["https://17k.com"]

    # 在爬虫开始的时候 给引擎传递第一个请求对象requests
    # 重写父类的statr_requests
    # 可以自己随意更改第一个请求的设计逻辑
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
            'Cookie': 'GUID=383cb3dc-a385-469a-b235-3168a4708a33; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22383cb3dc-a385-469a-b235-3168a4708a33%22%2C%22%24device_id%22%3A%2218f6aa8cf21329-0b1a8627c3e035-76574611-1049088-18f6aa8cf2276%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; acw_tc=2760828717155136720357968e4cd2f78e3ebd3de6aefee930accc60780c45',
            'Referer': '',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
        }
        for i in range(1, 334):
            headers['Referer'] = f'https://www.17k.com/all/book/2_0_0_0_0_0_0_0_{i}.html'
            url = f'https://www.17k.com/all/book/2_0_0_0_0_0_0_0_{i}.html'
            yield Request(url, callback=self.parse, headers=headers)

    def parse(self, resp, **key):
        # print(resp.text)
        text = resp.xpath('//td[@class="td3"]//a[@class="jt"]/text()').extract()
        print(text)
