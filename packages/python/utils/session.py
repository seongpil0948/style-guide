import sys, os, re
from bs4 import BeautifulSoup as bs
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class RetrySession(Session):
    __attrs__ = [
        'headers', 'cookies', 'auth', 'proxies', 'hooks', 'params', 'verify',
        'cert', 'prefetch', 'adapters', 'stream', 'trust_env',
        'max_redirects', 'retries', 'backoff', 'timeout', 'set_encoding',
        'mount', 'encoding'
    ]

    def __init__(self, retries=3, backoff=0.3, timeout=5, **kwargs):
        """ Session with retrying adapter
        param:
            retries: maximum number of retries (default: 3)
            backoff: sleep for {backoff} * 2 ** {n_retries}, (default: 0.3)
            timeout: request timeout
            encoding: if given, set response encoding after receiving requests
        """
        self.retries = retries
        self.backoff = backoff
        self.timeout = timeout
        self.set_encoding = ('encoding' in kwargs)
        self.encoding = None
        if self.set_encoding:
            self.encoding = kwargs['encoding']

        super().__init__()
        retry = Retry(retries, retries, retries, backoff_factor=backoff)
        adapter = HTTPAdapter(max_retries=retry)
        self.mount('https://', adapter)
        self.mount('http://', adapter)

    def request(self, method, url, **kwargs):
        if 'timeout' not in kwargs:
            kwargs['timeout'] = self.timeout

        r = super().request(method, url, **kwargs)

        if self.set_encoding:
            r.encoding = self.encoding

        return r.text