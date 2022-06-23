#حقوق الملف @T_8_T_T @T_HUNDER
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

#حقوق الملف @T_8_T_T @T_HUNDER
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

#حقوق الملف @T_8_T_T @T_HUNDER
API_HASH = getenv("API_HASH", "XXXXX")
API_ID = int(getenv("API_ID", "XXXXX"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXXXX")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "XXXXX")
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/50f5cfbd494b902b74f1a.jpg")
BOT_NAME = getenv("BOT_NAME", "XXXXX")
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
OWNER_NAME = getenv("OWNER_NAME", "ELLIOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "T_8_T_T")
SOURCE_CODE = getenv("SOURCE_CODE", "https://dashboard.heroku.com/new?template=https://github.com/THUNDERMUSICC/MUSIC-TO-BACK.git")
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1439222689").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/CHVOTLX")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/T_HUNDER")


COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/EITHON1")
