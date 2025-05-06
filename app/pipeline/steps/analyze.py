# app/pipeline/steps/analyze.py

from typing import Any, List, Dict
from app.pipeline.runner import PipelineStep, StepContext
from app.llm.analyzer import analyze_post
from app.utils.logger import get_logger
import time

logger = get_logger(__name__)


class AnalyzePosts(PipelineStep):
    """
    Applies LLM analysis to each post and attaches result to post['analysis'].
    """

    def process(self, posts: List[Dict], context: StepContext) -> List[Dict]:
        """
        Analyze each post using Gemini and append results under 'analysis' key.

        :param posts: List of Reddit posts (already stored in DB)
        :param context: Shared context with DB
        :return: List of posts, each including 'analysis' key
        """
        analyzed_posts = []

        for i, post in enumerate(posts, 1):
            try:
                logger.debug(
                    f"Analyzing post #{i}: {post['id']} - {post['title'][:60]}"
                )
                analysis = analyze_post(post)
                time.sleep(5)  # Rate limit to avoid hitting API too fast

                # Verificar formato mínimo
                required_keys = {
                    "opportunity",
                    "type",
                    "market_or_niche",
                    "potential_competitors",
                    "notes",
                    "confidence",
                }
                if not required_keys.issubset(analysis.keys()):
                    raise ValueError(f"Incomplete analysis fields: {analysis}")

                post["analysis"] = analysis
                analyzed_posts.append(post)
                logger.debug(
                    f"Analysis complete: {post['id']} → {analysis['opportunity']}, confidence: {analysis['confidence']}"
                )
            except Exception as e:
                logger.warning(f"Failed to analyze post {post['id']}: {e}")

        logger.info(f"{len(analyzed_posts)} posts successfully analyzed.")
        return analyzed_posts
