# -*- coding: utf-8 -*-
from scrapy import signals


class NewsHttpProxyMiddleware(object):
    def __init__(self, http_proxy_key=None):
        self.http_proxy_key = http_proxy_key

    @classmethod
    def from_crawler(cls, crawler):
        redis = getattr(crawler.spider, 'redis', None)
        proxy_key = crawler.settings['SCRAPY_PROXY_IP_KEY']
        http_proxy = redis.lpop(proxy_key) if redis else []

        crawler.signals.connect(cls.close, signals.spider_closed)
        return cls(http_proxy)

    @classmethod
    def close(cls, spider, reason):
        # Origin thought finished proxy ip, push proxy ip to Queue when `spider` finished,
        # But don't have to do that, operate Queue `rpoplpush` method from redis
        pass

    def process_request(self, request, spider):
        # spider.setting with classmethod from_crawler method crawler.setting is same
        # `SCRAPY_PROXY_IP_KEY` key can get from the `settings` variable
        redis = getattr(spider, 'redis', None)

        if redis and self.http_proxy_key:
            http_proxy = redis.rpoplpush(self.http_proxy_key, self.http_proxy_key)
        else:
            http_proxy = None

        if http_proxy and 'proxy' not in request.meta:
            request.meta['proxy'] = 'http://' + http_proxy
