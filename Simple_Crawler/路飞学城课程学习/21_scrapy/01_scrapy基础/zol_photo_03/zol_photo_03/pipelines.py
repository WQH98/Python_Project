# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.pipelines.files import FilesPipeline
from scrapy import Request

class ZolPhoto03Pipeline:
    def process_item(self, item, spider):
        return item


# scrapy提供了图片下载的功能
class zol_img_download(ImagesPipeline):
    # 更换成以下内容
    # 发送网络请求的
    def get_media_requests(self, item, info):
        url = item['img_url']
        yield Request(url, meta={'filename': url})

    # scrapy帮我们完成路径的拼接
    def file_path(self, request, response=None, info=None, *, item=None):
        # 需要返回文件的路径 是字符串
        filename = request.meta['filename']
        filename = filename.split('/')[-1]
        return f'./img/{filename}'

    def item_completed(self, results, item, info):
        # 最后的收尾工作
        pass

