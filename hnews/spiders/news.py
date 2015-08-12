# -*- coding: utf-8 -*-
import scrapy
from hnews.items import HnewsItem

class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.ycombinator.com"]
    download_delay = 5 

    start_urls = (
        'http://news.ycombinator.com/',
    )

    def parse(self, response):
        for sel in response.xpath('//tr[@class="athing"]/td/a'):
            item = HnewsItem()
            item['title'] = sel.xpath('text()').extract()[0]
            item['href'] = sel.xpath('@href').extract()[0]
            yield item

        for href in response.xpath('//a[@rel="nofollow" and text() = "More"]'):
           yield scrapy.Request(response.urljoin(href.xpath('@href').extract()[0]) , callback=self.parse)


