from pyrogram import Client
from Unzip.config import Config


app = Client(
    "unzip_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=dict(root="Unzip")
)
