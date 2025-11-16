import os
from dotenv import load_dotenv

load_dotenv()

TARGET_URL = os.getenv("TARGET_URL")
OUTPUT_FILE = os.getenv("OUTPUT_FILE")
USER_AGENT = os.getenv("USER_AGENT", "SIAG-Scraper/1.0")
