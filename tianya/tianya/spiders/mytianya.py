
import re
import scrapy
from tianya import items

class MytianyaSpider(scrapy.Spider):
    name = 'mytianya'
    allowed_domains = ['bbs.tianya.cn']
    start_urls = ['http://bbs.tianya.cn/post-140-393968-1.shtml']

    #主要逻辑与清洗过程
    def parse(self,response):

        html = response.body.decode('utf-8')
        #text 字符串类型  body二进制流数据
        #邮箱正则
        emailre = '[a-z0-9_]+@[a-z0-9]+\.[a-z]{2,4}'
        emailList = re.findall(emailre,html,re.I)  #忽略大小写
        #实例化item对象

        # item['email'] = emailList
        for email in emailList:
            item = items.TianyaItem()
            item['email'] = email
            print(item)
            yield item