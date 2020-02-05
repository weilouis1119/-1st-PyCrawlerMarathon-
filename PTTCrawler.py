# -*- coding: utf-8 -*-
import scrapy


class PttcrawlerSpider(scrapy.Spider):
    name = 'PTTCrawler'
    allowed_domains = ['www.ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Baseball/index.html']
    cookies={'over18':'1'}

    def parse(self, response):
      for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=self.cookies)
     def parse(self, response):
        pass
        




       
    
#https://www.ptt.cc/bbs/Baseball/index.html
        