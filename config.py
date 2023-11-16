import os
import logging
from logging.handlers import RotatingFileHandler


# Get a bot token from botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6643363347:AAGt8cOiwVRVHMM9fHvqFnfcG1J0Gn9YtDw")

# Get from my.telegram.org 
APP_ID = int(os.environ.get("APP_ID", "15898846"))

# Get from my.telegram.org 
API_HASH = os.environ.get("API_HASH", "8ddd6065c9101ac2678ef29437ec8dd7")

# Generate a user session string 
TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQDymN4Aiz4nGHfE9PsAV43wB5qu9Rpme03Ex45Z8k_R9Mnfx1fPVoUeuATPhHLD91bwN_-562CDPBSGzt1UOpE1C_fEz09rUfyzOx0DUDY0gxEvjwWnqnwND_65tiZg9qlFHPL6ia-MUL6DThLTDNno_h5lzYdrfL0WUbVhShLLqX_uNuxwyUmYzmoM1U5FWYBCGLfNfTtMIebfQd95uYe2f41oivm27qAPpx-sYo0SUworPjVjGKTq9fUBG7Q41z2uqjWJ3fGMgz_8MDFcx3sPkyJh4jSnHLOT3dBz32MEonMRerxijOfWTdQaFnnvHEuyWKDXWyk9XhQtw4v0TZVAz9hHCQAAAAE96hcYAA")

# ID of Channel from which the bot shoul search files
MAINCHANNEL_ID = os.environ.get("MAINCHANNEL_ID", "-1001838891399")




TG_BOT_SESSION = os.environ.get("TG_BOT_SESSION", "bot")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
LOG_FILE_NAME = "filterbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
