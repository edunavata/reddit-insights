# app/pipeline/steps/fetch.py

from typing import Any, List, Dict
from app.pipeline.runner import PipelineStep, StepContext
from app.reddit.fetcher import get_new_posts
from app.utils.logger import get_logger
import json

logger = get_logger(__name__)


class FetchRedditPosts(PipelineStep):
    """
    Fetches posts from Reddit for configured subreddits.
    """

    def __init__(
        self, subreddits: List[str] = ["askreddit", "worldnews"], limit: int = 20
    ):
        self.subreddits = subreddits
        self.limit = limit

    def process(self, data: Any, context: StepContext) -> List[Dict]:
        """
        Retrieve new Reddit posts from configured subreddits.

        :param data: Ignored (first step)
        :param context: Shared pipeline context (e.g., DB)
        :return: List of post dictionaries
        """
        logger.info(f"Fetching posts from subreddits: {self.subreddits}")
        posts = get_new_posts(self.subreddits, self.limit)
        logger.info(f"Fetched {len(posts)} posts in total.")

        # Mostrar preview de algunos posts
        preview = posts[:3]
        logger.debug("Sample posts retrieved:")
        for i, post in enumerate(preview, 1):
            summary = {
                "id": post.get("id"),
                "title": post.get("title"),
                "subreddit": post.get("subreddit"),
                "author": post.get("author"),
                "created_utc": post.get("created_utc"),
            }
            logger.debug(f"Post #{i}:\n{json.dumps(summary, indent=2)}")

        return posts
