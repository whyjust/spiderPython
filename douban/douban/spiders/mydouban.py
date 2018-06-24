# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from douban.items import DoubanItem


class MydoubanSpider(scrapy.Spider):
    name = 'mydouban'
    url = ['https://movie.douban.com/top250']
    start_urls = {'https://movie.douban.com/top250'} #方法1

    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)
    '''

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')

        for movie in movies:
            item['name'] = movie.xpath(".//div[@class='pic']/a/img/@alt").extract()[0]
            item['movieInfo'] = movie.xpath(".//div[@class='info']/div[@class='bd']/p/text()").extract()[0].strip()
            item['star'] = movie.xpath(".//div[@class='info']/div[@class='bd']/div[@class='star']/span[2]/text()").extract()[0]
            item['quote'] = movie.xpath('.//div[@class="star"]/span/text()').re(r'(\d+)人评价')[0]
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url,callback=self.parse)

