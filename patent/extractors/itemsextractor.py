# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re


class Base(object):
    rules = [
        re.compile(r'\s+', re.S)
    ]

    def __init__(self, items_list):
        self._items = items_list

    @property
    def filters(self):
        new_items = []

        for item in self._items:
            for _rule in self.rules:
                item = _rule.sub('', item)
            new_items.append(item)
        return new_items

    @property
    def values(self):
        return ''.join(self.filters)

    def _gen_key_pinyin(self, pairs_kv):
        pass


class PatentName(Base):
    """
    解析专利名称
    """


class PatentAbstract(Base):
    """
    解析专利的摘要文字
    """


class PatentOthers(Base):
    """
    解析专利的其他字段， 包括专利号， 时间地砖， 专利人等等
    """
    @property
    def items(self):
        """
        专利申请号是代表该项专利的唯一标示
        :return: dict
        """
        data = []
        patent_key = '申请号'
        others_list = self.filters

        for _item in others_list:
            delimiter = re.compile(r'[:：]').split(_item, 1)

            if len(delimiter) == 1:
                pairs = data.pop()
                data.append([pairs[0], pairs[1] + _item])
            else:
                data.append(delimiter)
        result = dict(data)

        # 判断专利申请号
        result['uuid'] = result.get(patent_key)
        return result
