from snakemd import Document
import logging
import feedparser

logger = logging.getLogger(__name__)


def get_recent_posts() -> list:
    """
    Collects current posts from The Renegade Coder. 

    :return: a list of posts from the How to Python series
    """
    url = "https://therenegadecoder.com/feed/"
    feed = feedparser.parse(url).entries
    logger.debug(f"Collected {len(feed)} posts")
    return feed

if __name__ == "__main__":
    posts = get_recent_posts()
    logging.basicConfig(level=logging.DEBUG)
    logger.debug(posts)
