import time
from random import randint


class AutoDelayMiddleware(object):
    def process_request(self, request, spider):
        if hasattr(spider, 'req_count'):
            req_count = getattr(spider, 'req_count')
        else:
            req_count = 1
        setattr(spider, 'req_count', req_count + 1)

        if req_count and req_count % 4 == 0:
            time.sleep(randint(2, 6))



