# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
import requests
import time


class LoginMiddleware(object):
    def process_request(self,request,spider):
        if spider.name == 'myzhihu':
            #判断是否登录
            if request.url.find('login') != -1:
                spider.browser = webdriver.Chrome()
                spider.browser.get(request.url)

                spider.browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/h3/a').click()
                time.sleep(3)
                username = spider.browser.find_element_by_name('username')
                password = spider.browser.find_element_by_name('password')

                username.send_keys('18588403840')
                time.sleep(2)
                password.send_keys('Changeme_123')
                time.sleep(2)
                spider.browser.find_element_by_xpath('//*[@id="fm1"]/input[8]').click()
                time.sleep(2)

                #获取登录后的cookie
                spider.cookies = spider.browser.get_cookies()
                return HtmlResponse(url=spider.browser.current_url,  # 当前url
                                    body=spider.browser.page_source,  # html源码
                                    encoding='utf-8')
            else:
                session = requests.session()  # 保存cookie
                # 设置cookie
                for cookie in spider.cookies:
                    # name, value
                    session.cookies.set(cookie['name'], cookie['value'])
                # 清空头
                session.headers.clear()

                # 响应
                response = session.get(url=request.url)

                return HtmlResponse(url=response.url,
                                    body=response.text,
                                    encoding='utf-8')






class ZhihuSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhihuDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
