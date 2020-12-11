from aiohttp import ClientSession
from bs4 import BeautifulSoup, Tag
from .constants import SOUNDCLOUD_KEYGEN_URL_REGEX, SOUNDCLOUD_API_KEY_REGEX, BASE_URL
from typing import List

async def gen_client_id(client: ClientSession) -> str:
    key = ""

    async with client.get(BASE_URL) as res:
        soup = BeautifulSoup(await res.text(), "lxml")
        urls: List[str] = [
            script["src"]
            for script in soup.select("script[crossorigin]")
            if SOUNDCLOUD_KEYGEN_URL_REGEX.match(script["src"])
        ]

    for url in urls:
        async with client.get(url) as res:
            data = await res.text()
            if ',client_id:"' in data:
                a = data.split(',client_id:"')
                key = a[1].split('"')[0]
                break
    return key