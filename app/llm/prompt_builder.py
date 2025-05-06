from typing import Dict


def build_prompt(post: Dict) -> str:
    """
    Builds a prompt to analyze a Reddit post for business opportunity signals using a rigorous methodology.

    :param post: Reddit post dictionary
    :type post: Dict
    :returns: Formatted prompt string
    :rtype: str
    """
    return f"""
        You are a business analyst AI. Your task is to determine if a Reddit post represents a genuine business opportunity. Use a structured and critical method to evaluate the post. Avoid optimism bias and only flag real, analyzable potential.

        ### Use the following rigorous criteria:

        1. **Problem Identification** — Is a clear, non-trivial problem or pain point stated or implied?
        2. **Solution Potential** — Does the post hint at or request a solution, or propose one?
        3. **Market Context** — Is there a well-defined group of people/businesses affected by the problem or interested in the idea?
        4. **Intent or Signal** — Is there an intention to act (build, explore, validate, launch, monetize)?
        5. **Differentiation/Gap** — Does the post suggest something unique, lacking, or unserved?

        Based on these, assess the post and respond strictly in the following JSON-like format (no markdown, no bullets):

        Opportunity: Yes or No
        Type: One of [Problem, Solution, Idea, Feedback, Other]
        Market_or_niche: Short description
        Potential_competitors: Brief list or N/A
        Notes: Insightful paragraph justifying your assessment using the 5 criteria above
        Confidence (0 to 1): A number from 0 to 1 representing your confidence in this being a real opportunity

        Now analyze the following post:

        Title: {post['title']}
        Content: {post['content']}
        Subreddit: {post['subreddit']}
        Flair: {post.get('flair')}
        Upvotes: {post['score']}, Comments: {post['num_comments']}
        URL: {post['url']}
    """
