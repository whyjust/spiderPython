# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class SinaPipeline(object):

    def __init__(self):
        self.conn = None
        self.cursor = None

    def open_spider(self,spider):
        self.conn = pymysql.connect(host='111.230.169.107',user='root',password='20111673',database='sina', port=3306,charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # sql = 'insert into sina_news(newsTitle,newsUrl,newsTime,content) VALUES (%r,%r,%r,%r)'%(item['newsTitle'], item['newsUrl'], item['newsTime'], item['content'])
        # self.cursor.execute(sql)
        # self.conn.commit()

        cols, values = zip(*item.items())
        sql = "INSERT INTO `%s` (%s) VALUES (%s)" % \
              (
                  'sina_news',
                  ','.join(cols),
                  ','.join(['%s'] * len(values))
              )
        self.cursor.execute(sql, values)
        self.conn.commit()
        print(self.cursor._last_executed)
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()