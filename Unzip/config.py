import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", ))
    API_HASH = os.environ.get("API_HASH", "")
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    
