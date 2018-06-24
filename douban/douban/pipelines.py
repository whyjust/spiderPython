# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class DoubanPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='111.230.169.107', port=3306, user= 'root', passwd = '20111673', database = 'douban',charset = 'utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute("truncate table Movie")
        self.conn.commit()

    def process_item(self, item, spider):
        try:
            self.cursor.execute("insert into Movie (name,movieInfo,star,quote) VALUES (%s,%s,%s,%s)",(item['name'], item['movieInfo'], item['star'], item['quote']))
            self.conn.commit()

        except pymysql.Error:
            print("Error%s,%s,%s,%s" % (item['name'], item['movieInfo'], item['star'], item['quote']))
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
