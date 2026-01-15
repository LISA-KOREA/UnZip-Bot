import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("7970441104:AAEiaUoJb0CG-rdz8eFDha5KYwAd6F6IfjY", "")
    API_ID = int(os.environ.get("20401115", ))
    API_HASH = os.environ.get("f27d722a2772cc581435be607be35022", "")
    MAX_FILE_SIZE = 2194304000
    
    
