# -*- coding: utf-8 -*-
import scrapy


class MyzhihuSpider(scrapy.Spider):
    name = 'myzhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://passport.csdn.net/account/login',
                  'https://mp.csdn.net/']

    def __init__(self):
        self.browser = None
        self.cookies = None
        super(MyzhihuSpider,self).__init__()

    def parse(self, response):
        print(response.body.decode('utf-8'))
