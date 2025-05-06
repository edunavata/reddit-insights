# app/pipeline/steps/store_analysis.py

from typing import Any, List, Dict
from app.pipeline.runner import PipelineStep, StepContext
from app.db.crud import create_post_analysis
from app.utils.logger import get_logger

logger = get_logger(__name__)


class StoreAnalysis(PipelineStep):
    """
    Stores the LLM analysis results for each post in the database.
    """

    def process(self, posts: List[Dict], context: StepContext) -> List[Dict]:
        """
        For each post, store its 'analysis' content in the database.

        :param posts: List of posts with `post["analysis"]` attached
        :param context: Contains DB session
        :return: List of posts for possible downstream steps
        """
        db = context.db
        saved = 0
        failed = 0

        for post in posts:
            post_id = post["id"]
            analysis_data = post.get("analysis")

            if not analysis_data:
                logger.warning(f"No analysis found for post {post_id}, skipping.")
                failed += 1
                continue

            try:
                create_post_analysis(db, post_id, analysis_data)
                logger.debug(f"Stored analysis for post {post_id}")
                saved += 1
            except Exception as e:
                logger.warning(f"Failed to store analysis for post {post_id}: {e}")
                failed += 1

        logger.info(f"{saved} analyses stored, {failed} failed.")
        return posts
