import time
import urllib
import urllib2
from random import choice

from patent.config.conf import USER_AGENT


class HtmlLoader(object):
    @staticmethod
    def get_raw_html(url, data=None, **kwargs):
        for i in range(1, 4):
            req = urllib2.Request(url) if not data else urllib2.Request(url, urllib.urlencode(data))
            req.add_header('User-Agent', choice(USER_AGENT))

            for head_value in kwargs.itervalues():
                for key, value in head_value.iteritems():
                    req.add_header(key, value)

            try:
                response = urllib2.urlopen(req, timeout=30)
                feed_data = response.read()
                response.close()
                return feed_data
            except Exception:
                time.sleep(3)
        return '<html></html>'

