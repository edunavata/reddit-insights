from app.db.session import SessionLocal
from app.db import crud
from app.reddit.fetcher import get_new_posts
from app.llm.analyzer import analyze_post
from app.utils.clean_analysis_keys import clean_analysis_keys
import time


def run_pipeline():
    db = SessionLocal()
    posts = get_new_posts(["startups", "Entrepreneur"], limit=10)

    for post in posts:
        if crud.get_post(db, post["id"]):
            continue  # skip already processed posts

        try:
            # Guardar post
            crud.create_post(db, post)

            # Análisis LLM
            analysis = clean_analysis_keys(analyze_post(post))

            # Guardar análisis
            crud.create_post_analysis(db, post["id"], analysis)
            print(f"✅ Procesado: {post['title']}")
            time.sleep(5)

        except Exception as e:
            print(f"⚠️ Error: {e} - Post: {post['title']}")
