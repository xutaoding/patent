# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector

from .preurls import PreUrls
from ..items.items import PatentItem
from ..extractors.simpleextractor import ItemsExtractors


class PatentSpider(scrapy.Spider):
    name = 'sipo'

    def __init__(self, rtype='fmgb', start=None, end=None):
        """
        初始化Spider
        :param rtype: string, 专利类型
        :param start:  int, 抓取的开始页数
        :param end: int, 抓取的结束页数
        """
        self.start_urls = PreUrls(rtype).get_start_urls(start, end)
        super(PatentSpider, self).__init__(self.name)

    def parse(self, response):
        block_css = 'div.cp_linr'

        for each_block in response.css(block_css).extract():
            extractor = ItemsExtractors(Selector(text=each_block))
            items = extractor.patent_items
            yield PatentItem(**items)
