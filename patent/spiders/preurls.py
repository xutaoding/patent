# -*- coding: utf-8 -*-
import re
import urllib

from patent.utils import HtmlLoader
from patent.config import ConfPatent


class PreUrls(object):
    def __init__(self, rtype):
        self._conf_instance = ConfPatent(rtype)
        self._pairs_rule = re.compile(r'pato\.(?P<key>.*?)\.value\s+=\s+"(?P<value>.*?)";')

    def get_start_urls(self, start_pages=None, end_pages=None):
        """
        得到开始到结束的链接， 以供爬虫
        :param start_pages: int, 开始页数
        :param end_pages: int, 结束页数
        :return:
        """
        params = {}
        total_items = 1
        start_pages = int(start_pages) if start_pages else 1

        default_page = 'page_now'
        url = self._conf_instance.get_start_qs()
        html = HtmlLoader.get_raw_html(url)

        for key, value in self._pairs_rule.findall(html):
            if key == 'pageNow':
                params[key] = default_page
            else:
                params[key] = value

            if value.isdigit() and int(value) > total_items:
                total_items = int(value)

        div, mod = divmod(total_items, self._conf_instance.page_size)
        total_pages = div + (mod and 1)
        pagination = total_pages if end_pages is None else int(end_pages)

        base_url = self._conf_instance.base_url + '?' + urllib.urlencode(params)
        return [base_url.replace(default_page, str(p)) for p in xrange(start_pages, pagination + 1)]


if __name__ == '__main__':
    PreUrls('fmgb').get_start_urls()
    # PreUrls('fmsq').get_start_urls()
    # PreUrls('syxx').get_start_urls()
    # PreUrls('wgsj').get_start_urls()

