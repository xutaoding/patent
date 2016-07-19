# -*- coding: utf-8 -*-
import re
import urllib
from datetime import date

import conf


class ConfPatent(object):
    base_url = conf.BASE_URL
    page_size = conf.DEFAULT_PAGE_SIZE

    def __init__(self, rtype='fmgb'):
        """
        :param rtype: 每种发明的类型首拼音
        """
        assert rtype in self.conf_mapping

        self.rtype = rtype
        self.rtype_conf = getattr(conf, self.rtype.upper() + '_CONF', None)

    @property
    def source(self):
        return {'fmgb': 'pip', 'fmsq': 'pig', 'syxx': 'pug', 'wgsj': 'pdg'}

    @property
    def conf_mapping(self):
        return {'fmgb': '发明公布', 'fmsq': '发明授权', 'syxx': '实用新型', 'wgsj': '外观设计'}

    @staticmethod
    def _urlencode(query_string):
        params = {}

        for item in query_string.split('&'):
            k, v = item.split('=', 1)
            params[k] = v
        return urllib.urlencode(params)

    def get_start_qs(self):
        """
        获得各种类型发明的总数和更正数或解密数
        :return:
        """
        key_regex = re.compile(r'\{(.*?)\}')
        kv_args = ['='.join(item) for item in self.rtype_conf.iteritems()]
        qs = '&'.join(kv_args)
        default_kw = {'dt_start': '1949.10.01', 'total': '0', 'dt_end': date.today().strftime('%Y.%m.%d')}

        required_kw = {key: default_kw.get(key, '') for key in key_regex.findall(qs)}
        return self.base_url + '?' + self._urlencode(qs.format(**required_kw))


if __name__ == '__main__':
    url = ConfPatent().get_start_qs()
    print url

