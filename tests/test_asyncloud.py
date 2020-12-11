import pytest
from aiohttp import ClientSession
import asyncloud

def test_version():
    assert asyncloud.__version__ == '0.1.0'

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
        assert user["id"] == 468563046

@pytest.mark.asyncio
async def test_track():
    """
    https://soundcloud.com/bagelboy-305309012/astleys-paradise
    """
    async with ClientSession(raise_for_status=True) as session:
        client_id = await asyncloud.gen_client_id(session)
        client = asyncloud.SoundCloud(client_id, session)
        track = await client.track(654315092)
        assert track["id"] == 654315092
