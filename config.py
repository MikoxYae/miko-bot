import os
import random

APP_ID = int(os.environ.get("APP_ID", "28614709"))
API_HASH = os.environ.get("API_HASH", "f36fd2ee6e3d3a17c4d244ff6dc1bac8")
OWNER = os.environ.get("OWNER", "Anythingbutnew56")
OWNER_ID = int(os.environ.get("OWNER_ID", "8229041976"))
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Payal:Aloksingh@payal.jv2kwch.mongodb.net/?appName=Payal")
DB_NAME = os.environ.get("DATABASE_NAME", "Angle")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8717980062:AAGf3y0VFNtxUE0vQdYVkgI4CQrBPW6_zAU")

_start_pics_env = os.environ.get("START_PIC", "")
START_PICS = [p.strip() for p in _start_pics_env.split() if p.strip()] or [
    "https://graph.org/file/061b0e3db0d196e59a4fe-2a8738290ab4203df1.jpg",
    "https://graph.org/file/061b0e3db0d196e59a4fe-2a8738290ab4203df1.jpg",
    "https://graph.org/file/8f0eeb1a57eba9b0d8268-8871415b5cfa8b11ca.jpg",
]

def get_start_pic():
    return random.choice(START_PICS)

START_MSG = os.environ.get(
    "START_MSG",
    "Hello {first}! 👋\n\nI'm **{bot_name}**.\n\nHow can I help you today?"
)
