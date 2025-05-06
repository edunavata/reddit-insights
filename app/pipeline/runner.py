from app.reddit.fetcher import get_new_posts
from app.llm.analyzer import analyze_post


def run_pipeline():
    posts = get_new_posts(["Entrepreneur", "startups"], limit=5)

    for post in posts:
        analysis = analyze_post(post)
        print("\n--- POST ---")
        print(post["title"])
        print("--- ANALYSIS ---")
        print(analysis)
