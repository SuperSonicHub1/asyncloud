from aiohttp import ClientSession
from .constants import BASE_API_URL
import asyncio
from typing import Optional, List


class SoundCloud:
    session: ClientSession
    client_id: str

    def __init__(
        self, client_id: str, session: ClientSession = ClientSession()
    ) -> None:
        self.session = session
        self.client_id = client_id

    async def user(self, user_id: int) -> dict:
        """
        Returns a user.
        """
        url = BASE_API_URL / "users" / str(user_id) % {"client_id": self.client_id}
        async with self.session.get(url) as res:
            return await res.json()

    async def track(self, track_id: int) -> dict:
        """
        Returns a track.
        """
        url = BASE_API_URL / "tracks" / str(track_id) % {"client_id": self.client_id}
        async with self.session.get(url) as res:
            return await res.json()
    
    async def tracks(self, track_ids: List[int]) -> List[dict]:
        """
        Returns multiple tracks.
        https://api-v2.soundcloud.com/tracks?ids=597556383,650566580,654315092,656196194,676168613,679236228,685073137,694108864,716251402
        """
        pass
