import typing

import httpx

from youtubesearchpython.core.constants import userAgent


class RequestCore:
    def __init__(
        self,
        proxy: typing.Union[typing.Dict, str],  # = None,
    ):
        self.url = None
        self.data = None
        self.timeout = 2
        self.proxy = proxy
        # print(f"{__name__} ::{self.proxy=}")

    def syncPostRequest(self) -> httpx.Response:
        res = httpx.get(
            "https://httpbin.org/ip",
            headers={"User-Agent": userAgent},
            timeout=self.timeout,
            proxies=self.proxy,
        )
        print(f"{res.json()=}")
        return httpx.post(
            self.url,
            headers={"User-Agent": userAgent},
            json=self.data,
            timeout=self.timeout,
            proxies=self.proxy,
        )

    async def asyncPostRequest(self) -> httpx.Response:
        async with httpx.AsyncClient(proxies=self.proxy) as client:
            r = await client.post(
                self.url,
                headers={"User-Agent": userAgent},
                json=self.data,
                timeout=self.timeout,
            )
            return r

    def syncGetRequest(self) -> httpx.Response:
        return httpx.get(
            self.url,
            headers={"User-Agent": userAgent},
            timeout=self.timeout,
            cookies={"CONSENT": "YES+1"},
            proxies=self.proxy,
        )

    async def asyncGetRequest(self) -> httpx.Response:
        async with httpx.AsyncClient(proxies=self.proxy) as client:
            r = await client.get(
                self.url,
                headers={"User-Agent": userAgent},
                timeout=self.timeout,
                cookies={"CONSENT": "YES+1"},
            )
            return r
