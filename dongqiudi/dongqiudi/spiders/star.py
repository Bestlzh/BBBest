# -*- coding: utf-8 -*-
import scrapy


class StarSpider(scrapy.Spider):
    name = 'star'
    allowed_domains = ['http://www.dongqiudi.com/']
    start_urls = ['http://www.dongqiudi.com/']
    def parse(self, response):
        print('aaaaaaaaaaaaaaaaaaa')
        links = response.xpath('//*[@id="rank_list"]/table/tr/td[2]/a/@href').extract()
        for link in links:

            request = scrapy.Request(link,callback = self.parse_star,headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'})

            yield request

    def parse_star(self,response):
        name = response.xpath('//*[@id="con"]/div/div[1]/div[1]/div[2]/div/div/h1/text()').extract_first()
        star = response.xpath('//*[@id="con"]/div/div[1]/div[3]/table/tbody/tr/td[3]/a/span/text()').extract_first()
        print(name)
        print(star)


