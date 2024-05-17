from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup




@Client.on_message(filters.command("start"))
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📍 Update Channel", url="https://t.me/NT_BOT_CHANNEL"),
        ],
        [
            InlineKeyboardButton("👥 Support Group", url="https://t.me/NT_BOTS_SUPPORT"),
            InlineKeyboardButton("👩‍💻 Developer", url="https://t.me/LISA_FAN_LK"),
        ] 
   ]
  )
    start_message = (
        "Hello!\n\n"
        "Send me a ZIP file, and I'll unzip it for you."
    )
    await message.reply(start_message, reply_markup=reply_markup)
