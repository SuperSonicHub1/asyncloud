from yarl import URL
from re import compile

BASE_URL = URL("https://soundcloud.com")
BASE_API_URL = URL("https://api-v2.soundcloud.com")
SOUNDCLOUD_KEYGEN_URL_REGEX = compile(
    r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
)
# SOUNDCLOUD_API_KEY_REGEX = compile(
#     r"(https:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
# )
