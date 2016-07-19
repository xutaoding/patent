from scrapy.spidermiddlewares.offsite import OffsiteMiddleware


class MewsSpiderMiddleware(object):
    pass
    # def process_start_requests(self, start_requests, spider):
        # print 'haHah:', start_requests
        # print 'spider midd:', type(start_requests)
        # return start_requests
        # if 'config_key' not in response.meta:
        #     print 'ggg:', response.url
        #     response.meta['config_key'] = 'abcdefg'

