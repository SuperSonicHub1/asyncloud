from aiohttp import ClientSession
from .constants import BASE_API_URL
import asyncio
from typing import Optional, List
from types import SimpleNamespace


class SoundCloud:
    session: ClientSession
    client_id: str

    def __init__(
        self, client_id: str, session: ClientSession = ClientSession()
    ) -> None:
        self.session = session
        self.client_id = client_id

    async def user(self, user_id: int) -> SimpleNamespace:
        """
        Returns a user.
        """
        url = BASE_API_URL / "users" / str(user_id) % {"client_id": self.client_id}
        async with self.session.get(url) as res:
            return SimpleNamespace(**(await res.json()))

    async def track(self, track_id: int) -> SimpleNamespace:
        """
        Returns a track.
        """
        url = BASE_API_URL / "tracks" / str(track_id) % {"client_id": self.client_id}
        async with self.session.get(url) as res:
            return SimpleNamespace(**(await res.json()))

    async def tracks(self, track_ids: List[int]) -> List[SimpleNamespace]:
        """
        Returns multiple tracks.
        """
        url = (
            BASE_API_URL
            / "tracks"
            % {
                "ids": ",".join([str(track_id) for track_id in track_ids]),
                "client_id": self.client_id,
            }
        )
        async with self.session.get(url) as res:
            return [SimpleNamespace(**track) for track in (await res.json())]

    async def resolve(self, resource_url: str) -> SimpleNamespace:
        url = (
            BASE_API_URL
            / "resolve"
            % {"url": resource_url, "client_id": self.client_id}
        )
        async with self.session.get(url) as res:
            return SimpleNamespace(**(await res.json()))
