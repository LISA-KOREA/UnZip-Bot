from pyrogram import Client
from Unzip.config import Config


app = Client(
    "unzip_bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    plugins=dict(root="Unzip")
)


print("🎊 I AM ALIVE 🎊  • Support @NT_BOTS_SUPPORT")
app.run()
