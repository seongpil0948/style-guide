from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
import asyncio
import aiohttp

class RetrySession(Session):
    def __init__(
        self,
        retries=3,
        backoff=0.3,
        timeout=5,
        encoding=None,
    ):
        self.retries = retries
        self.backoff = backoff
        self.timeout = timeout
        self.encoding = encoding
        super().__init__()
        retry = Retry(retries, retries, retries, backoff_factor=backoff)
        adapter = HTTPAdapter(max_retries=retry)
        self.mount("https://", adapter)
        self.mount("http://", adapter)

        self.headers["User-Agent"] = "SNU IDS Lab (http://ids.snu.ac.kr/)"

    def request(self, method, url, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout
        r = super().request(method, url, **kwargs)
        if self.encoding is not None:
            r.encoding = self.encoding
        return r
 
    
