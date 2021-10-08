import logging
import random
from datetime import datetime

import feedparser
import subete
from snakemd import Document, InlineText, MDList, Paragraph
from subete.repo import SampleProgram

repo = subete.load()
logger = logging.getLogger(__name__)
emojis = [
    ":fu:",
    ":exclamation:",
    ":notes:",
    ":cat:",
    ":seedling:",
    ":milky_way:",
    ":lock:",
    ":door:",
    ":gem:",
    ":tea:",
    ":dango:"
]


def get_recent_posts() -> list:
    url = "https://therenegadecoder.com/feed/"
    feed = feedparser.parse(url).entries
    logger.debug(f"Collected {len(feed)} posts")
    return feed


def get_code_snippet() -> SampleProgram:        
    code = repo.random_program()
    return code


def generate_readme(posts: list, code: SampleProgram) -> Document:
    readme = Document("README")
    readme.add_header("Welcome to My Profile!")
    readme.add_paragraph(f"This week's code snippet, {code}, is brought to you by Subete and the Sample Programs repo.") \
        .insert_link("Subete", url="https://subete.therenegadecoder.com/en/latest/") \
        .insert_link("Sample Programs repo", url="https://sample-programs.therenegadecoder.com/")
    readme.add_code(code.code().encode("ascii", "ignore").decode("ascii").strip(), lang=code.language())
    readme.add_paragraph("Below you'll find an up-to-date list of articles by me on The Renegade Coder.") \
        .insert_link("The Renegade Coder", "https://therenegadecoder.com")
    readme.add_element(MDList([Paragraph([random.choice(emojis), " ", InlineText(post.title, url=post.link)]) for post in posts]))
    readme.add_paragraph("Also, here are some fun links you can use to support my work.")
    readme.add_element(MDList([
        InlineText("Patreon", url="https://www.patreon.com/TheRenegadeCoder"),
        InlineText("Discord", url="https://discord.gg/Jhmtj7Z"),
        InlineText("Mailing List", url="https://newsletter.therenegadecoder.com/"),
        InlineText("Twitter", url="https://twitter.com/RenegadeCoder94"),
        InlineText("YouTube", url="https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw")
    ]))
    readme.add_horizontal_rule()
    now = datetime.today().strftime('%Y-%m-%d')
    readme.add_paragraph(f"This document was automatically rendered on {now} using SnakeMD.") \
        .insert_link("SnakeMD", "https://snakemd.therenegadecoder.com")
    return readme


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    posts = get_recent_posts()
    code = get_code_snippet()
    readme = generate_readme(posts, code)
    readme.output_page("")