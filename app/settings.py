import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CSRID_API_URL = os.getenv("CSRID_API_URL")

if not TOKEN or not CSRID_API_URL:
    raise ValueError("TELEGRAM_BOT_TOKEN or CSRID_API_URL is not set in .env file")
