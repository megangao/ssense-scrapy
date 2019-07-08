# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SsenseItem(scrapy.Item):
    brand = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
