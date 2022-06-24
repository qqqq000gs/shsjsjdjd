import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_IMAGE, BOT_USERNAME, OWNER_USERNAME, UPDATES_CHANNEL, SUPPORT_GROUP, SOURCE_CODE
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 مرحبا انا بوت 
استطيع تشغيل الميوزك في المحادثات  
وايضا استطيع تشغيل الفديو.
┏━━━━━━━━━━━━━━━━━┓                                      
┣❥︎ OWNER ➪ » [المالك](https://t.me/{OWNER_USERNAME})
┣❥︎ BOTS ➪ » [تنصيب بوت]({SOURCE_CODE})
┣❥︎ UPDATE ➪ » [التحديثات]({UPDATES_CHANNEL})
┣❥︎ SUPORRT ➪ » [الدعم]({SUPPORT_GROUP})
┗━━━━━━━━━━━━━━━━━┛
💞 اضفني الي مجموعتك
واستمتع بجوده عاليه في التشغيل.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ اضفني الي مجموعتك ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", f"start@{BOT_USERNAME}", "/alive", ".alive", "#bikash", "#aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 💥 انضم الي جروب الدعم 💞", url=f"{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "تنصيب", "bikash", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/50f5cfbd494b902b74f1a.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 اضغط هنا لتنصيب بوتك 💞", url=f"{SOURCE_CODE}")
                ]
            ]
        ),
    )
