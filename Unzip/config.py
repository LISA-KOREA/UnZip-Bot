import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7951305676:AAFExtyFSrU_Ao9E7DWj9m6geEyO9CFcoXk")
    API_ID = int(os.environ.get("API_ID",'22911604' ))
    API_HASH = os.environ.get("API_HASH", "cb27e2111bb65de1cacddb7738645425")
    
    
