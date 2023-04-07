import logging
import random
from datetime import datetime

import feedparser
import subete
from snakemd import Document, Inline, MDList, Paragraph

repo = subete.load()
logger = logging.getLogger(__name__)


def get_recent_posts() -> list:
    """
    Retrieves the list of posts from The Renegade Coder RSS feed,

    :return: a list of posts
    """
    logging.debug("Retrieving recent posts from The Renegade Coder")
    url = "https://therenegadecoder.com/feed/"
    feed = feedparser.parse(url)
    logger.debug(f"Loaded feed: {feed}")
    entries = feed.entries
    logger.debug(f"Collected {len(entries)} posts")
    return entries


def get_code_snippet() -> subete.SampleProgram:
    """
    Retrieves a random code snippet from the Sample Programs repo.

    :return: a sample program object
    """
    logger.debug("Loading sample programs repo")
    code = repo.random_program()
    return code


def _get_emoji(page_link: str):
    emojis = {
        "blog": ":black_nib:",
        "code": ":computer:",
        "meta": ":milky_way:",
        "teach": ":apple:"
    }
    overlap = set(page_link.split("/")).intersection(emojis.keys())
    return emojis[list(overlap)[0]]
    

def generate_readme(posts: list, code: subete.SampleProgram) -> Document:
    """
    Generates the README document from a list of posts and a sample program.

    :param posts: a list of posts
    :param code: a code snippet
    :return: a markdown document to be rendered
    """
    readme = Document()
    readme.add_heading("Welcome to My Profile!")
    readme.add_paragraph(f"This week's code snippet, {code}, is brought to you by Subete and the Sample Programs repo.") \
        .insert_link("Subete", url="https://subete.jeremygrifski.com/en/latest/") \
        .insert_link("Sample Programs repo", url="https://sampleprograms.io/")
    readme.add_code(
        code.code().encode("ascii", "ignore").decode("ascii").strip(),
        lang=code.language_name()
    )
    readme.add_paragraph(
        """
        Below you'll find an up-to-date list of articles by me on The Renegade Coder.
        For ease of browsing, emojis let you know the article category (i.e., blog: 
        :black_nib:, code: :computer:, meta: :milky_way:, teach: :apple:)
        """
    ).insert_link("The Renegade Coder", "https://therenegadecoder.com")
    readme.add_block(MDList([
        Paragraph([
            _get_emoji(post.link),
            " ",
            Inline(post.title, link=post.link)
        ])
        for post in posts
    ]))
    readme.add_paragraph(
        "Also, here are some fun links you can use to support my work."
    )
    readme.add_block(MDList([
        Inline("Patreon", link="https://www.patreon.com/TheRenegadeCoder"),
        Inline("Discord", link="https://discord.gg/Jhmtj7Z"),
        Inline("Mailing List", link="https://therenegadecoder.com/about/newsletter"),
        Inline("Twitter", link="https://twitter.com/RenegadeCoder94"),
        Inline("YouTube", link="https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw")
    ]))
    readme.add_horizontal_rule()
    now = datetime.today().strftime('%Y-%m-%d')
    readme.add_paragraph(f"This document was automatically rendered on {now} using SnakeMD.") \
        .insert_link("SnakeMD", "https://www.snakemd.io")
    return readme


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    posts = get_recent_posts()
    code = get_code_snippet()
    readme = generate_readme(posts, code)
    readme.dump("README")
