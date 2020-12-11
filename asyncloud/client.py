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
        """Returns a user.

        Args:
            user_id (int): SoundCloud user ID

        Returns:
            SimpleNamespace: User
        """
        url = BASE_API_URL / "users" / str(user_id) % {"client_id": self.client_id}
        async with self.session.get(url) as res:
            return SimpleNamespace(**(await res.json()))

    async def track(self, track_id: int) -> SimpleNamespace:
        """Returns a track.

        Args:
            track_id (int): SoundCloud track ID

        Returns:
            SimpleNamespace: Track
        """
        url = BASE_API_URL / "tracks" / str(track_id) % {"client_id": self.client_id}
        async with self.session.get(url) as res:
            return SimpleNamespace(**(await res.json()))

    async def tracks(self, track_ids: List[int]) -> List[SimpleNamespace]:
        """Returns multiple tracks.

        Args:
            track_ids (List[int]): List of SoundCloud track IDs

        Returns:
            List[SimpleNamespace]: List of tracks
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

    async def resolve(self, sc_url: str) -> SimpleNamespace:
        """Resolves soundcloud.com URLs to Resource URLs to use with the API.

        Args:
            sc_url (str): Soundcloud URL

        Returns:
            SimpleNamespace: SoundCloud resource
        """
        url = (
            BASE_API_URL
            / "resolve"
            % {"url": sc_url, "client_id": self.client_id}
        )
        async with self.session.get(url) as res:
            return SimpleNamespace(**(await res.json()))

    async def playlist(self, playlist_id: int) -> SimpleNamespace:
        url = BASE_API_URL / "playlists" / str(playlist_id) % {"client_id": self.client_id}
        async with self.session.get(url) as res:
            return SimpleNamespace(**(await res.json()))
