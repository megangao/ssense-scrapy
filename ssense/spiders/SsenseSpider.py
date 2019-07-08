# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from ssense.items import SsenseItem

SsenseURL = "https://www.ssense.com/en-us/women/sale" # scrape women's sale

class SsenseSpider(scrapy.Spider):
    name = 'SsenseSpider'
    allowed_domains = ['ssense.com']
    start_urls = [SsenseURL]

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="browsing-product-list"]//figure[contains(@class,"browsing-product-item")]')
        for product in products:
            item = SsenseItem()
            item['brand'] = product.xpath('.//a/figcaption/p[1]/text()').get(),
            item['name'] = product.xpath('normalize-space(.//a/figcaption/p[2]/text())').get(),
            item['price'] = product.xpath('.//div/p/span[2]/text()').get(),
            item['link'] = product.xpath('.//meta[3]/@content').get(),
            item['image_urls'] = product.xpath('.//img[1]/@data-srcset').get(),
            yield item
            
        # in development: call to next page
        # next_page = response.css('ul.nav li.last-page li').xpath('//@href').get(),
        # logging.debug(next_page)
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)