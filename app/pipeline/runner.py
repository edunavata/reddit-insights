# app/pipeline/runner.py

from app.reddit.fetcher import get_new_posts


def run_pipeline():
    """
    Main function to orchestrate the Reddit insights pipeline.
    """
    subreddits = ["Entrepreneur", "startups"]
    posts = get_new_posts(subreddits=subreddits, limit=5)

    for post in posts:
        print(f"[{post['subreddit']}] {post['title']}\n→ {post['url']}\n")
