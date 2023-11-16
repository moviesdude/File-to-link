# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '16229284'))
    API_HASH = str(getenv('API_HASH', 'ebd1fead3cc15343bea10b5c164165ba'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6488689300:AAH6TCrcskFOMi2rFtD6nHQPK4Ninog9qUM'))
    name = str(getenv('name', 'Fast_Downloader_bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002008584034'))
    PORT = int(getenv('PORT', '8080'))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1103137195").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'md_test2_bot'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', 'BIND_ADRESS:PORT')) if not ON_HEROKU or getenv('FQDN', '') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://moviesdudebot:MDbots@cluster0.y4gwugw.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'chutti_TV_Tamil_HD'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1002008584034")).split()))      
    SHORTLINK_URL = getenv('SHORTLINK_URL', 'onepagelink.in')
    SHORTLINK_API = getenv('SHORTLINK_API', '88860a074bf831cf78e2e7dfbade22eb05a5c2fb')
    TUTORIAL_URL = getenv('TUTORIAL_URL', 'https://t.me/Demoshorts')
