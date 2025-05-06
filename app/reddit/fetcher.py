from typing import List, Dict
from .client import get_reddit_client


def get_new_posts(subreddits: List[str], limit: int = 20) -> List[Dict]:
    """
    Fetches the most recent posts from the specified subreddits.

    :param subreddits: List of subreddit names to retrieve posts from.
    :type subreddits: List[str]
    :param limit: Number of posts to fetch per subreddit.
    :type limit: int
    :returns: List of post dictionaries, each containing the following fields:

        - **id** (*str*): Unique Reddit ID of the post.
        - **title** (*str*): Title of the post.
        - **content** (*str*): Text content of the post (empty if it's a link post).
        - **author** (*str*): Reddit username or "[deleted]" if unavailable.
        - **created_utc** (*float*): UTC timestamp of post creation.
        - **url** (*str*): Full URL of the post content.
        - **permalink** (*str*): Reddit permalink to the post.
        - **subreddit** (*str*): Name of the subreddit.
        - **flair** (*str | None*): Flair/tag associated with the post, if any.
        - **score** (*int*): Net score (upvotes - downvotes).
        - **upvote_ratio** (*float*): Ratio of upvotes to total votes.
        - **num_comments** (*int*): Number of comments on the post.
        - **is_self** (*bool*): True if post is self/text type.
        - **nsfw** (*bool*): True if marked as Not Safe For Work.
        - **subreddit_subscribers** (*int | None*): Number of subscribers in the subreddit.

    :rtype: List[Dict[str, Any]]
    """
    reddit = get_reddit_client()
    posts = []

    for subreddit_name in subreddits:
        subreddit = reddit.subreddit(subreddit_name)
        for submission in subreddit.new(limit=limit):
            posts.append(
                {
                    "id": submission.id,
                    "title": submission.title,
                    "content": submission.selftext,
                    "author": (
                        str(submission.author) if submission.author else "[deleted]"
                    ),
                    "created_utc": submission.created_utc,
                    "url": submission.url,
                    "permalink": f"https://reddit.com{submission.permalink}",
                    "subreddit": str(submission.subreddit),
                    "flair": submission.link_flair_text,
                    "score": submission.score,
                    "upvote_ratio": submission.upvote_ratio,
                    "num_comments": submission.num_comments,
                    "is_self": submission.is_self,
                    "nsfw": submission.over_18,
                    "subreddit_subscribers": getattr(
                        submission.subreddit, "subscribers", None
                    ),
                }
            )

    return posts
