"""An asynchronous SoundCloud API wrapper that doesn't need an API key."""
__version__ = '0.1.0'

from .client import SoundCloud
from .utility import gen_client_id
from . import classes
