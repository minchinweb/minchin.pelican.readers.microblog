from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pelican import Pelican
    from pelican.generators import ArticlesGenerator

from jinja2.utils import url_quote
from markupsafe import Markup

from pelican.contents import Article
from pelican.readers import MarkdownReader  # BaseReader
from pelican.utils import order_content

from .constants import DEFAULT_MICROBLOG_CATEGORY, LOG_PREFIX

# from pelican.utils import get_date, pelican_open


logger = logging.getLogger(__name__)

_micropost_count = 0


def addMicroArticle(articleGenerator: ArticlesGenerator) -> None:
    global _micropost_count

    settings = articleGenerator.settings

    # Author, category, and tags are objects, not strings, so they need to
    # be handled using myBaseReader's process_metadata() function.
    # myBaseReader = BaseReader(settings)
    myMarkdownReader = MarkdownReader(settings)
    myBaseReader = myMarkdownReader

    file_extensions = [
        "txt",
    ] + MarkdownReader.file_extensions

    for post in articleGenerator.get_files(
        paths=settings["MICROBLOG_FOLDER"], extensions=file_extensions
    ):
        post = settings["PATH"] + os.sep + post

        content, metadata = myMarkdownReader.read(source_path=post)
        # count length on content before adding tag and image links
        linkless_content = content

        new_article_metadata = {
            "category": myBaseReader.process_metadata(
                "category",
                settings.get("MICROBLOG_CATEGORY", DEFAULT_MICROBLOG_CATEGORY),
            ),
            # "tags": myBaseReader.process_metadata("tags", "tagA, tagB"),
            "micro": myBaseReader.process_metadata("micro", True),
        }

        post_slug = settings["MICROBLOG_SLUG"].format(**metadata)
        metadata["slug"] = post_slug

        try:
            new_article_metadata["author"] = myBaseReader.process_metadata(
                "author", settings["AUTHOR"]
            )
        except KeyError:
            # if author isn't set by either the general settings or the
            # micropost metadata, we don't need to force one
            pass

        new_article_metadata["title"] = myBaseReader.process_metadata(
            "title", post_slug
        )
        new_article_metadata["date"] = metadata["date"]
        new_article_metadata["slug"] = post_slug
        new_article_metadata["save_as"] = myBaseReader.process_metadata(
            "save_as", settings["MICROBLOG_SAVE_AS"].format(**metadata)
        )
        new_article_metadata["url"] = myBaseReader.process_metadata(
            "url", settings["MICROBLOG_URL"].format(**metadata)
        )

        if "image" in metadata.keys():
            new_article_metadata["image"] = myBaseReader.process_metadata(
                "image", metadata["image"]
            )

            # add image link to end of content

            image_url = f'{settings["SITEURL"]}'
            image_url += "/" if not settings["SITEURL"].endswith("/") else ""
            image_url += url_quote(metadata["image"])  # Jinja filter "urlencode"

            image_link = f'<a href={image_url} class="microblog-post-image">{image_url}</a>'

            content = content.removesuffix("</p>") + " " + image_link + "</p>"

        if "tags" in metadata.keys():
            # new_article_metadata["tags"] = myBaseReader.process_metadata("tags", metadata["tags"])
            new_article_metadata["tags"] = metadata["tags"]

            if settings.get("MICROBLOG_APPEND_HASHTAGS", True):
                # metadata["tags"] is already a list of `pelican.urlwrappers.Tag`
                for tag in metadata["tags"]:
                    tag_url = settings["SITEURL"] + "/" + tag.url
                    tag_link = f'<a href="{tag_url}" class="microblog-post-tag">#{tag.name}</a>'

                    content = content.removesuffix("</p>") + " " + tag_link + "</p>"

        # warn if too long
        # ignore added tag and image links here
        safe_content = Markup(linkless_content).striptags()
        post_len = len(safe_content)
        # why the plus six here??
        if post_len > settings["MICROBLOG_MAX_LENGTH"] + 6:
            relative_filename = post.removeprefix(settings["PATH"])
            logger.warning(
                '%s micropost "%s" longer than expected (%s > %s).',
                LOG_PREFIX,
                relative_filename,
                post_len,
                settings["MICROBLOG_MAX_LENGTH"],

            )
        new_article_metadata["char_len"] = post_len

        # print(post_len)

        # NOTE:
        # new_article_metadata is set by pelicanconf.py
        # metadata is set from the microblog post and is given higher precedence below.
        new_article_metadata.update(metadata)

        new_article = Article(
            content,
            new_article_metadata,
        )

        articleGenerator.articles.insert(0, new_article)
        _micropost_count += 1

    # apply sorting
    logger.debug('%s sorting order: "%s"', LOG_PREFIX, settings.get("ARTICLE_ORDER_BY", "reversed-date"))
    self.articles = order_content(
        self.articles, settings.get("ARTICLE_ORDER_BY", "reversed-date")
    )


def pelican_finalized(pelican: Pelican) -> None:
    global _micropost_count
    print(
        "%s Processed %s micropost%s."
        % (LOG_PREFIX, _micropost_count, "s" if _micropost_count != 1 else ""),
    )
