import scrapy.cmdline

def main():
    # -o  ['json', 'jsonlines', 'jl', 'csv', 'xml', 'marshal', 'pickle']
    scrapy.cmdline.execute(['scrapy','crawl','mysina'])

if __name__ == '__main__':
    main()