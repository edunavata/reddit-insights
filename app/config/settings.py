# app/config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

DB_URL = os.getenv("DATABASE_URL", "sqlite:///reddit.db")

# Otros parámetros configurables
DEFAULT_SUBREDDITS = os.getenv("DEFAULT_SUBREDDITS", "Entrepreneur,startups").split(",")
POST_FETCH_LIMIT = int(os.getenv("POST_FETCH_LIMIT", 20))
