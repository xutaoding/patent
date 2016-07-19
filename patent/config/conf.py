# -*- coding: utf-8 -*-

DEFAULT_PAGE_SIZE = 20
BASE_URL = 'http://epub.sipo.gov.cn/patentoutline.action'

# 发明公布的基本配置
FMGB_CONF = {
    'showType': '1',
    'strSources': '{source}',
    'strWhere': "OPD=BETWEEN['{dt_start}','{dt_end}']",
    'numSortMethod': '{sort_mth}',
    'strLicenseCode': '',
    'numIp': '{total}',     # 发明公布总数
    'numIpc': '{gzh}',      # 发明公布更正
    'numIg': '',
    'numIgc': '',
    'numIgd': '',
    'numUg': '',
    'numUgc': '',
    'numUgd': '',
    'numDg': '',
    'numDgc': '',
    'pageSize': str(DEFAULT_PAGE_SIZE),
    'pageNow': '{page}'
}

# 发明授权的基本配置
FMSQ_CONF = {
    'showType': '1',
    'strSources': '{source}',
    'strWhere': "OPD=BETWEEN['{dt_start}','{dt_end}']",
    'numSortMethod': '{sort_mth}',
    'strLicenseCode': '',
    'numIp': '',
    'numIpc': '',
    'numIg': '{total}',         # 发明授权总数
    'numIgc': '{gzh}',          # 发明授权更正
    'numIgd': '{jiemi}',        # 发明解密
    'numUg': '',
    'numUgc': '',
    'numUgd': '',
    'numDg': '',
    'numDgc': '',
    'pageSize': str(DEFAULT_PAGE_SIZE),
    'pageNow': '{page}'
}

# 实用新型的基本配置
SYXX_CONF = {
    'showType': '1',
    'strSources': '{source}',
    'strWhere': "OPD=BETWEEN['{dt_start}','{dt_end}']",
    'numSortMethod': '{sort_mth}',
    'strLicenseCode': '',
    'numIp': '',
    'numIpc': '',
    'numIg': '',
    'numIgc': '',
    'numIgd': '',
    'numUg': '{total}',           # 实用新型总数
    'numUgc': '{gzh}',            # 实用新型更正
    'numUgd': '',
    'numDg': '',
    'numDgc': '',
    'pageSize': str(DEFAULT_PAGE_SIZE),
    'pageNow': '{page}'
}


# 外观设计的基本配置
WGSJ_CONF = {
    'showType': '1',
    'strSources': '{source}',
    'strWhere': "OPD=BETWEEN['{dt_start}','{dt_end}']",
    'numSortMethod': '{sort_mth}',
    'strLicenseCode': '',
    'numIp': '',
    'numIpc': '',
    'numIg': '',
    'numIgc': '',
    'numIgd': '',
    'numUg': '',
    'numUgc': '',
    'numUgd': '',
    'numDg': '{total}',     # 外观设计总数
    'numDgc': '{gzh}',        # 外观设计更正
    'pageSize': str(DEFAULT_PAGE_SIZE),
    'pageNow': '{page}'
}

# Mongo Base Settings
HOST = '192.168.100.20'
PORT = 27017
DB = 'py_crawl'
TABLE = 'patent'


USER_AGENT = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36',

    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0',

    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b11pre) Gecko/20110128 Firefox/4.0b11pre',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b11pre) Gecko/20110131 Firefox/4.0b11pre',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b11pre) Gecko/20110129 Firefox/4.0b11pre',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b11pre) Gecko/20110128 Firefox/4.0b11pre',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0b11pre) Gecko/20110126 Firefox/4.0b11pre',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b10pre) Gecko/20110118 Firefox/4.0b10pre',
]

