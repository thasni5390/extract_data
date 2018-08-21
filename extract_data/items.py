# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ExtractDataItem(scrapy.Item):
    # define the fields for your item here like:
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    size = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()
