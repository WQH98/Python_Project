# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class Lottery02Pipeline:
    def __init__(self):
        self.f = None

    # 开关两个函数名必须是这么写的 框架规定好的
    def open_spider(self, spider):
        self.f = open('./data.csv', 'a', encoding='utf-8')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        self.f.write(item['issue'])
        self.f.write(', ')
        self.f.write('_'.join(item['red']))
        self.f.write(', ')
        self.f.write(item['blue'])
        self.f.write('\n')
        return item


class Lottery02Pipeline_MySQL:
    # 开关两个函数名必须是这么写的 框架规定好的
    def __init__(self):
        self.conn = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(user='root', password='admin', host='localhost', port=3306, database='scrapy')

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        try:
            # 写个游标
            cursor = self.conn.cursor()
            # 写入数据
            sql = 'insert into lottery(issue, red, blue) values (%s, %s, %s)'
            cursor.execute(sql, (item['issue'], '_'.join(item['red']), item['blue']))
            # 提交事务
            self.conn.commit()
        except Exception as e:
            print(e)
            # 回滚
            self.conn.rollback()
        return item
