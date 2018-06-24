import requests
from lxml import etree
import time
# import random
# import ssl
#
#
# context = ssl._create_unverified_context()
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
        i = 1
        html = self.session.get(self.url+str(i), headers=self.headers).text

        mytree = etree.HTML(html)
        tableList = mytree.xpath("//div[@id='list']//tbody/tr")
        http_ips = []
        for tr in tableList[1:]:
            type1 = tr.xpath("./td[@data-title='类型']/text()")[0]
            ipDict = {'ip': '', 'port': ''}
            if type1 == 'HTTP':
                ip = tr.xpath("./td[@data-title='IP']/text()")[0]
                port = tr.xpath("./td[@data-title='PORT']/text()")[0]

                ipDict['ip'] = ip
                ipDict['port'] = port
                http_ips.append(ipDict)

        return http_ips

class Main(object):

    def __init__(self,url,ip):
        self.url = url
        self.proxies = {
            'http': 'http://' + ip['ip'] + ':' + ip['port']
        }

    def work(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
        }

        response = requests.get(url=url,headers=headers,proxies=self.proxies)
        print(response.status_code,response.text)


if __name__ == '__main__':
    get_ip = Get_ip()
    http_ips = get_ip.run()
    url = 'https://www.cnblogs.com/why957/p/9213246.html'
    for ip in  http_ips:
        time.sleep(2)
        print(ip)
        main = Main(url,ip)
        main.work()

