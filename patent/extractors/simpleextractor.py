# -*- coding: utf-8 -*-
"""
解析专利网页的数据
"""

from ..settings.sipo_settings import SIPO_FILTERING as _FILTERING


class ItemsExtractors(object):
    def __init__(self, selector):
        """
        :param selector: scrapy Selector class instance
        """
        self._selector = selector

    @staticmethod
    def simple_filtering(data_list):
        return [item.strip() for item in data_list if item.strip() and item.strip() not in _FILTERING]

    @property
    def patent_name(self):
        name_xpath = './/h1/text()'
        name_list = self._selector.xpath(name_xpath).extract()
        return {'name': self.simple_filtering(name_list)}

    @property
    def patent_abstract(self):
        abs_xpath = '//div[@class="cp_jsh"]//text() '
        abstract_list = self._selector.xpath(abs_xpath).extract()
        return {'abstract': self.simple_filtering(abstract_list)}

    @property
    def patent_others(self):
        others_xpath = './/li//text()'
        other_list = self._selector.xpath(others_xpath).extract()
        return {'others': self.simple_filtering(other_list)}

    @property
    def patent_items(self):
        items = {}
        items.update(**self.patent_name)
        items.update(**self.patent_abstract)
        items.update(**self.patent_others)
        return items



