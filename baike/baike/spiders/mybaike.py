# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from baike.items import BaikeItem


class MybaikeSpider(CrawlSpider):
    name = 'mybaike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/Python/407313']

    rules = [Rule(LinkExtractor(allow=('item/(.*)')),callback='getParse',follow=True)]

    def getParse(self, response):
        level1Title = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h1/text()")[0].extract()
        level2Title = response.xpath("//dd[@class='lemmaWgt-lemmaTitle-title']/h2/text()")
        if len(level2Title) != 0:
            level2Title = level2Title[0].extract()
        else:
            level2Title = '待编辑'
        contentList = response.xpath("//div[@class='lemma-summary']//text()")
        content = ''
        for c in contentList:
            content += c.extract()
            print(content)

        item = BaikeItem()
        item['level1Title'] = level1Title
        item['level2Title'] = level2Title
        item['content'] = content

        yield item

