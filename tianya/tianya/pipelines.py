# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TianyaPipeline(object):
    '''
    存储,返回值一定为item
    '''

    #开启爬虫调用
    def open_spider(self,spider):
        self.f = open('mytianya.text','a+',encoding='utf-8',errors='ignore')

    def process_item(self, item, spider):
        self.f.write(item['email'] + '\n')
        return item

    #关闭爬虫
    def close_spider(self,spider):
        self.f.close()
