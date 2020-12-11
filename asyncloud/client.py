from aiohttp import ClientSession
from bs4 import BeautifulSoup, Tag
from .constants import BASE_URL, BASE_API_URL, SOUNDCLOUD_KEYGEN_URL_REGEX, SOUNDCLOUD_API_KEY_REGEX
import asyncio
from typing import Optional, List

class SoundCloud:
    session: ClientSession
    client_id: str

    def __init__(self, session: ClientSession = ClientSession(), client_id : Optional[str] = None) -> None:
        self.session = session
        if not client_id:
           asyncio.create_task(self._gen_client_id(internal=True))
        else:
            self.client_id = client_id
    
    async def _gen_client_id(self, internal: bool = False) -> str:
        key = ""

        async with self.session.get(BASE_URL) as res:
            soup = BeautifulSoup(res.content, "lxml")
            urls: List[str] = [script["src"] for script in soup.select_all("script[crossorigin]") if SOUNDCLOUD_KEYGEN_URL_REGEX.match(script["src"])]

        for url in urls:
            async with self.session.get(url) as res:
                data = await res.text()
                if ',client_id:"' in data:
                    a = data.split(',client_id:"')
                    key = a[1].split('"')[0]
                    break
        if internal:
            self.client_id = key
        return key
