from aiohttp import ClientSession
from .constants import BASE_API_URL
import asyncio
from typing import Optional


class SoundCloud:
    session: ClientSession
    client_id: str

    def __init__(
        self, client_id: str, session: ClientSession = ClientSession()
    ) -> None:
        self.session = session
        self.client_id = client_id
