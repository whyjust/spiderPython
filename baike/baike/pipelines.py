# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class BaikePipeline(object):
    def __init__(self):
        self.conn = None
        self.cousor = None

    def open_spider(self, spider):
        # 连接
        self.conn = pymysql.connect(host='111.230.169.107', user='root', password="20111673",
                                    database='baike', port=3306,
                                    charset='utf8')
        # 游标
        self.cousor = self.conn.cursor()

    def process_item(self, item, spider):

        cols, values = zip(*item.items())

        # `表名`
        sql = "INSERT INTO `%s`(%s) VALUES (%s)" % \
              ('baike', ','.join(cols), ','.join(['%s'] * len(values)))

        self.cousor.execute(sql, values)
        self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cousor.close()
        self.conn.close()
