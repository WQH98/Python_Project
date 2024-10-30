import scrapy
from scrapy.http.request import Request

"""
    补充一个拼接url的小知识
    抓到的url：/bizhi/9109_111583_2.html
    从这个页面抓到的url：https://desk.zol.com.cn/dongman/
    网站主页面是：https://desk.zol.com.cn/
    
    如果链接是以/开头 需要拼接的是域名 最前面的/是根目录
    此时要拼接的结果是：https://desk.zol.com.cn/bizhi/9109_111583_2.html
    
    如果链接不是以/开头 此时拼接的就是当前目录
    此时要拼接的结果是：https://desk.zol.com.cn/dongman/bizhi/9109_111583_2.html
    
    可以直接使用urllib中的urljoin方法
"""

class ZolPhotoSpider(scrapy.Spider):
    name = "zol_photo"
    allowed_domains = ["desk.zol.com.cn"]
    start_urls = ["https://desk.zol.com.cn/dongman/"]

    def parse(self, resp, **keys):
        urls = resp.xpath('//ul[@class="pic-list2  clearfix"]/li/a/@href').extract()
        for url in urls:
            if url.endswith('.exe'):
                continue
            # # 使用python提供的urllib模块
            # from urllib.parse import urljoin
            # url = urljoin(resp.url, url)
            # print(url)
            # 使用scrapy提供的方法
            url = resp.urljoin(url)
            print(url)
            # 在scrapy中 请求想要发出去 就必须经过引擎 -> 调度器 -> 引擎 -> 下载器
            # scrapy发送请求的固定逻辑 这个请求如果没有其它参数的话 也会自动调用parse
            # 我们需要做的事 告诉引擎 这次请求的响应应该调用谁
            yield Request(url, callback=self.zol_photo_parse)

    def zol_photo_parse(self, resp, **key):
        img_url = resp.xpath('//img[@id="bigImg"]/@src').extract_first()
        print(img_url)
        # 下载图片是在保存数据 可以交给管道进行保存
        # 也可以直接访问 保存
        yield {
            'img_url': img_url
        }
