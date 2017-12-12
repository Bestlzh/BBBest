# -*- coding: utf-8 -*-
import scrapy
from home58.items import HouseInfoItem
def filter(html):
    return html.replace('\t','').replace('\r\n','').replace('&nbsp;&nbsp;','').replace('   ','')


class HouseSpider(scrapy.Spider):
    name = 'house'
    allowed_domains = ['bj.58.com']
    start_urls = ['http://www.bj.58.com/chuzu/']


    def parse(self, response):

        # http://bj.58.com/chuzu/pn2/
        for i in range(6,63):
            link =  'http://bj.58.com/chuzu/pn' + str(i)
            request = scrapy.Request(link, callback=self.parse_houselist)
            yield request
            # print(link)

    def parse_houselist(self,response):
        response = response.replace(body=filter(response.text))
        links = response.xpath('/html/body/div[3]/div[1]/div[5]/div[2]/ul/li/div[2]/h2/a/@href').extract()
        for link in links:
            request = scrapy.Request(link, callback=self.parse_houseinfo)
            yield request
            # print(link)
    def parse_houseinfo(self,response):
        response = response.replace(body=filter(response.text))
        # response = response.replace(body = response.text)
        item = HouseInfoItem(
            price = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/div/span[1]/b/text()').extract()[0])

        info_keys = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li/span[1]/text()').extract()
        info_values_one = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li/span[2]/text()').extract()
        info_values_two = response.xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li/span[2]/a/text()').extract()

        info_values = info_values_one + info_values_two
        # print(info_values[1])
        # print(info_values[1][8:11])
        # print(info_values[1][-4:-1])

        print(info_values[1])

        item['lease_way'] = info_values[0]
        item['layout'] = info_values[1][0:6]
        item['square'] = info_values[1][8:11]
        print(info_values[1].split(' '))
        if len(info_values[1].split(' ')[4]) < 2:

            item['renovation'] = None
        else:
            item['renovation'] = info_values[1].split(' ')[4][1:]

        if len(info_values[2].split('/')[0]) == 4:

            item['floor'] = info_values[2][2:]
            item['direction'] = info_values[2][0:2]
        else:
            item['floor'] = info_values[2][1:]
            item['direction'] = info_values[2][0:1]
        item['village'] = info_values[-3]
        item['area'] = info_values[-2]
        item['address'] = info_values[-1]
        yield item




