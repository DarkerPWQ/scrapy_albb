# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AlbbItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    product_url=scrapy.Field()
    product_name = scrapy.Field()
    product_key1 = scrapy.Field()
    product_key2 = scrapy.Field()
    product_key3 = scrapy.Field()
# class productItem(scrapy.Item):
#     product_name = scrapy.Field()
