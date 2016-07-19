import random

from .base import USER_AGENT as _UA


class UserAgentMiddleware(object):
    def __init__(self):
        self.user_agent = _UA

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agent)

        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
