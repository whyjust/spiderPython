

import scrapy.cmdline

def main():
    scrapy.cmdline.execute(['scrapy','crawl','mytianya','-o','mytianya.json'])

if __name__ == '__main__':
    main()