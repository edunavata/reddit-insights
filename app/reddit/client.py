# app/reddit/client.py

from dotenv import load_dotenv
import os
import praw

load_dotenv()


def get_reddit_client() -> praw.Reddit:
    """
    Returns a Reddit client instance using credentials from environment variables.

    :returns: Configured Reddit client
    :rtype: praw.Reddit
    """
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT", "reddit-insights-bot/0.1"),
    )
