# -*- coding: utf-8 -*-
import scrapy
import requests
from lxml import etree
from sina import items

from scrapy.spiders import CrawlSpider,Rule  #CrawlSpiders:定义了一些规则跟进link
from scrapy.linkextractors import LinkExtractor  #提取链接

class MysinaSpider(CrawlSpider):
    name = 'mysina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_2.shtml']
    '''
    Rule参数:link_extractor, callback=None, cb_kwargs=None, follow=None, process_links=None, process_request=identity
    LinkExtractor部分参数: allow=(), deny=(), allow_domains=(), deny_domains=(), restrict_xpaths=()

    allow=(正则)允许的, deny=(正则)不允许的
    callback=回调
    follow= 跟随如果为True就跟随
    '''
    rules = [Rule(LinkExtractor(allow=('index_(\d+).shtml')),callback='getParse',follow=True)]

    def getParse(self, response):

        newsList = response.xpath("//ul[@class='list_009']/li")
        for news in newsList:

            # item = items.SinaItem()
            newsTitle = news.xpath('./a/text()')[0].extract()
            newsUrl = news.xpath('./a/@href')[0].extract()
            newsTime = news.xpath('./span/text()')[0].extract()
            # content = self.getContent(newsUrl)
            #构造请求
            request = scrapy.Request(newsUrl,callback=self.getMataContent)

            #存储到item对象
            # item['newsTitle'] = newsTitle
            # item['newsUrl'] = newsUrl
            # item['newsTime'] = newsTime
            # item['content'] = content
            # print(item)

            #使用meta传参
            request.meta['newsTitle'] = newsTitle
            request.meta['newsUrl'] = newsUrl
            request.meta['newsTime'] = newsTime
            # request.meta['content'] = content

            # yield item
            yield request

    # def getContent(self,url):
    #     headers = {
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
    #     }
    #     response = requests.get(url,headers=headers).content.decode('utf-8','ignore')   #content二进制
    #     mytree = etree.HTML(response)
    #     contentList = mytree.xpath("//div[@class='article']//text()")
    #     print(contentList)
    #     content = ''
    #     for c in contentList:
    #         # print(content.replace('\n',''))
    #         #Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    #         content += c.strip().replace('\n','')
    #     return content

    def getMataContent(self,response):

        contentList = response.xpath("//div[@class='article']//text()")
        content = ''
        for c in contentList:
            content += c.extract().strip()
        item = items.SinaItem()
        #通过response.meta
        item['newsTitle'] = response.meta['newsTitle']
        item['newsUrl'] = response.meta['newsUrl']
        item['newsTime'] = response.meta['newsTime']
        item['content'] = content

        yield item

