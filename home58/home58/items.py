# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Home58Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HouseInfoItem(scrapy.Item):

    lease_way= scrapy.Field()
    layout = scrapy.Field()
    square = scrapy.Field()
    renovation = scrapy.Field()
    price = scrapy.Field()
    floor = scrapy.Field()
    direction = scrapy.Field()
    village = scrapy.Field()
    area = scrapy.Field()
    address= scrapy.Field()

