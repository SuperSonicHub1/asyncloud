import pytest
from aiohttp import ClientSession
import asyncloud


def test_version():
    assert asyncloud.__version__ == "0.1.0"


# https://fastapi.tiangolo.com/advanced/async-tests/
@pytest.mark.asyncio
async def test_keygen():
    async with ClientSession(raise_for_status=True) as session:
        client_id = await asyncloud.gen_client_id(session)
    assert client_id


@pytest.mark.asyncio
async def test_user():
    """
    https://soundcloud.com/kyle-supersonicspy1
    """
    async with ClientSession(raise_for_status=True) as session:
        client_id = await asyncloud.gen_client_id(session)
        client = asyncloud.SoundCloud(client_id, session)
        user = await client.user(468563046)
    assert user.id == 468563046


@pytest.mark.asyncio
async def test_track():
    """
    https://soundcloud.com/bagelboy-305309012/astleys-paradise
    """
    async with ClientSession(raise_for_status=True) as session:
        client_id = await asyncloud.gen_client_id(session)
        client = asyncloud.SoundCloud(client_id, session)
        track = await client.track(654315092)
    assert track.id == 654315092


@pytest.mark.asyncio
async def test_tracks():
    """
    https://api-v2.soundcloud.com/tracks?ids=597556383,650566580
    https://soundcloud.com/tahutoa/tainted-love-by-soft-shell
    https://soundcloud.com/uun4/something-arrived-in-hell-today
    """
    track_ids = [597556383, 650566580]
    async with ClientSession(raise_for_status=True) as session:
        client_id = await asyncloud.gen_client_id(session)
        client = asyncloud.SoundCloud(client_id, session)
        tracks = await client.tracks(track_ids)
    for index, track in enumerate(tracks):
        assert track.id == track_ids[index]


@pytest.mark.asyncio
async def test_resolve():
    """
    https://soundcloud.com/sewerslvt/sets/the-world-is-fvcked
    """
    url = "https://soundcloud.com/sewerslvt/sets/the-world-is-fvcked"
    async with ClientSession(raise_for_status=True) as session:
        client_id = await asyncloud.gen_client_id(session)
        client = asyncloud.SoundCloud(client_id, session)
        album = await client.resolve(url)
    assert album.id == 1173509695

@pytest.mark.asyncio
async def test_playlist():
    """
    https://soundcloud.com/com-truise/sets/galactic-melt-1
    """
    async with ClientSession(raise_for_status=True) as session:
        client_id = await asyncloud.gen_client_id(session)
        client = asyncloud.SoundCloud(client_id, session)
        album = await client.playlist(331154216)
    assert album.id == 331154216
