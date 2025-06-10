import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7530089172:AAHiSyWR5PoVWFM-Siy-Ctnnym7Ddz8olAU")
    API_ID = int(os.environ.get("API_ID", "28918271"))
    API_HASH = os.environ.get("API_HASH", "29bf447b916a795191046a91317869fb")
    MAX_FILE_SIZE = 2194304000
    
    
