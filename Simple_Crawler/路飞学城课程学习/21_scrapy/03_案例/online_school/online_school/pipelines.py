# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class OnlineSchoolPipeline:
    def process_item(self, item, spider):
        file_path = item.get('file_path')
        file_name = item.get('file_name')
        question_info = item.get('question_info')
        path = f'./download/{file_path}'
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.join(path, file_name) + '.md', mode='a', encoding='utf-8') as f:
            f.write(question_info)
        # print('pipline获取到的数据========>', item)
        return item
