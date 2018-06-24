import requests
from bs4 import BeautifulSoup
import time
import re
import random
import xlwt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


class Get_ip(object):
    '''
    获取ip信息
    '''

    def __init__(self):
        super(Get_ip, self).__init__()
        self.url = 'http://www.kuaidaili.com/free/inha/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Accept": "*/*",
            "Connection": "Keep-Alive"

        }
        self.session = requests.session()

    def run(self):
        '''
        获取ip代理
        :return:
        '''
        html = self.session.get(self.url, headers=self.headers).text
        soup = BeautifulSoup(html, 'lxml')
        tableList = soup.select('#list > table')[0].find_all('tr')
        http_ips = []
        for tr in tableList[1:]:

            type = tr.select('td')[3].get_text()
            ipDict = {'ip': '', 'port': ''}
            if type == 'HTTP':
                ip = tr.select('td')[0].get_text()
                port = tr.select('td')[1].get_text()
                ipDict['ip'] = ip
                ipDict['port'] = port
                http_ips.append(ipDict)
            print(http_ips)
        return http_ips


class Get_urls():
    '''
    爬取每一页的url,并进入链接
    '''
    def __init__(self, url, page, ip):
        self.page = page
        self.url = url
        self.proxies = {
            'http': 'http://' + ip['ip'] + ':' + ip['port']
        }

    def get_url(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
        }
        print(self.url + '&beginPage=' + str(self.page))
        html = requests.get(self.url + '&beginPage=' + str(self.page),headers=headers, proxies=self.proxies).text
        print(html)

        soup = BeautifulSoup(html,'lxml')
        table = soup.find('div', attrs={'id': 'sw_mod_mainblock'}).find('url').find_all('div', attrs={'class': 'list-item-left'})
        urls = []
        for item in table:
            urls.append(item.find('a').get('href'))
        return urls


class Get_contact():
    '''
    链接1688批发网获取电话与链接信息
    '''
    def __init__(self, url, ip):
        self.proxies = {
            'http': 'http://' + ip['ip'] + ip['port']
        }
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
        }
        self.session = requests.session()

    def run(self):
        try:
            html = self.session.get(self.url, headers=self.headers, proxies=self.proxies, timeout=2).text
            contact_url = BeautifulSoup(html).find('div', attrs={'class': 'top-nav-bar-box'}).find('li', attrs={'data-page-name': 'contactinfo'}).find('a').get('href')
        except:
            self.statue = 0
            print('~~~')
            return
        self.statue = 1
        try:
            html = self.session.get(contact_url, headers=self.headers, proxies=self.proxies, timeout=2).text
            table = BeautifulSoup(html).find('div', attrs={'class': 'fd-line'}).find_all('dl')
            self.title = BeautifulSoup(html).find('div', attrs={'class': 'contact-info'}).find('h4').get_text()
            self.infor = []
            for item in table[:-1]:
                self.infor.append(item.get_text().replace('\n', '').replace('', ''))
        except:
            self.statue = 0

class Main():
    '''
    主函数
    '''
    def __init__(self):
        self.f = xlwt.Workbook()
        self.sheet = self.f.add_sheet('sheet')
        self.count = 0
        work = Get_ip()
        self.ips = work.run()

    def work(self):

        '''
        https://s.1688.com/company/company_search.htm?keywords=%BE%AB%C3%DC%BB%FA%D0%B5&earseDirect=false&button_click=top&n=y&pageSize=30&offset=3&beginPage=2

        '''
        search_url = 'https://s.1688.com/company/company_search.htm?keywords=%BE%AB%C3%DC%BB%FA%D0%B5&earseDirect=false&button_click=top&n=y&pageSize=30&offset=3'
        for i in range(4):
            url_get = Get_urls(search_url, i + 2, self.ips[random.randint(0, len(self.ips) - 1)])
            try:
                urls = url_get.get_url()
            except:
                continue
            for url in urls:
                spider = Get_contact(url, self.ips[random.randint(0, len(self.ips) - 1)])
                spider.run()
                if spider.statue == 0:
                    continue
                self.sheet.write(self.count, 0, spider.title)
                num = 1
                for infor in spider.infor:
                    self.sheet.write(self.count, num, infor)
                    num += 1
                self.count+=1
                print(self.count)
                self.f.save(r'F:\web项目\爬虫项目\1688\data.xls')

if __name__ == '__main__':
    work = Main()
    work.work()
