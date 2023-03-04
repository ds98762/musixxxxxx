## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID", "14300380"))
API_HASH = getenv("API_HASH", "40bc7e7cdfcd0e939cac0ed964884460")
OWNER_NAME = getenv("OWNER_NAME","𝙳 𝙷 𝙸 𝙼 𝙰 𝙽")
ALIVE_NAME = getenv("ALIVE_NAME", "🌿🌸 ❰ 𝐃ʜɪᴍᴀɴ ✘ 𝐀ssɪsᴛᴀɴᴛ ❱ 🍃🦋")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "S_0_P_H")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "About_vishu")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/b2b4fee33e6c7d2a5651a.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ds98762")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/b2b4fee33e6c7d2a5651a.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/b2b4fee33e6c7d2a5651a.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/b2b4fee33e6c7d2a5651a.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/b2b4fee33e6c7d2a5651a.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/b2b4fee33e6c7d2a5651a.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/b2b4fee33e6c7d2a5651a.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/b2b4fee33e6c7d2a5651a.jpg")
