# -*- coding: utf-8 -*-
import scrapy
from ..items import WandoujiaItem


class WandouSpider(scrapy.Spider):
    name = 'wandoujia'
    allowed_domains = ['www.wandoujia.com']
    start_urls = []
    for i in range(1, 6):
        url = "http://www.wandoujia.com/search/16717912156701033019_page"
        url = url + str(i)
        start_urls.append(url)

    def parse(self, response):
        items = []
        for each in response.xpath('//div[@class="col-left"]//li[@class="search-item search-searchitems"]'):
            item = WandoujiaItem()
            name = each.xpath('./a/@data-app-name').extract()
            package = each.xpath('./a/@data-app-pname').extract()
            item['name'] = name
            item['package'] = package
            items.append(item)
        return items
