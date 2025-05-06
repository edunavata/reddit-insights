# app/pipeline/steps/filter.py

from typing import Any, List, Dict
from app.pipeline.runner import PipelineStep, StepContext
from app.db.crud import get_post, create_post
from app.utils.logger import get_logger

logger = get_logger(__name__)


class FilterAndStoreNewPosts(PipelineStep):
    """
    Filters out existing posts and stores new ones in the database.
    """

    def process(self, posts: List[Dict], context: StepContext) -> List[Dict]:
        """
        For each post:
        - Check if it exists in DB.
        - If not, create it and keep it for further processing.

        :param posts: List of Reddit post dicts
        :param context: Shared context with DB session
        :return: List of new posts that were stored and need analysis
        """
        db = context.db
        new_posts = []
        skipped = 0
        created = 0

        for post in posts:
            if get_post(db, post["id"]):
                logger.debug(
                    f"Skipping existing post: {post['id']} - {post['title'][:60]}"
                )
                skipped += 1
            else:
                try:
                    create_post(db, post)
                    new_posts.append(post)
                    created += 1
                    logger.debug(
                        f"Stored new post: {post['id']} - {post['title'][:60]}"
                    )
                except Exception as e:
                    logger.warning(f"Failed to create post {post['id']}: {e}")

        logger.info(f"{skipped} posts skipped, {created} new posts stored.")
        return new_posts
