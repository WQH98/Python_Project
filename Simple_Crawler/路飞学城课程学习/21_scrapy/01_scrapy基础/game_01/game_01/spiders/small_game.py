import scrapy


# 声明了一个类 继承自scrapy默认的Spider
class SmallGameSpider(scrapy.Spider):
    # 爬虫的名字
    name = "small_game"
    # 当前爬虫允许访问的域名是
    # 只要是不符合这个域名规则的url scrapy会自动屏蔽掉
    allowed_domains = ["4399.com"]
    # 起始url 第一个要访问的url
    start_urls = ["https://www.4399.com/flash/"]

    # 默认的数据解析的位置 -> 主要负责第一个url的解析工作
    def parse(self, response):
        li_list = response.xpath('//ul[@class="n-game cf"]/li')
        for li in li_list:
            name = li.xpath('./a/b/text()').extract_first()
            category = li.xpath('./em/a/text()').extract_first()
            game_time = li.xpath('./em/text()').extract_first()
            # print(name, '\t', category, '\t', game_time)
            # 可以返回数据 而不打断函数的执行 比return好
            # Spider must return request, item, or None
            # 返回值必须是 请求对象 数据 或者不返回
            # 可以返回字典 充当item
            # 数据会经过引擎 传递给管道
            yield {
                'name': name,
                'category': category,
                'game_time': game_time,
            }

