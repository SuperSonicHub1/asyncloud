import pytest
from aiohttp import ClientSession
import asyncloud

def test_version():
    assert asyncloud.__version__ == '0.1.0'

# https://fastapi.tiangolo.com/advanced/async-tests/
@pytest.mark.asyncio
async def test_keygen():
    async with ClientSession() as session:
        client_id = await asyncloud.gen_client_id(session)
    assert client_id
