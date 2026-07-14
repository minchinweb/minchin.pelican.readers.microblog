"""
Supporting invoke tasks.
"""

import sys
from pathlib import Path

from minchin.pelican.readers.microblog import __version__
from minchin.pelican.readers.microblog.constants import LOG_PREFIX


try:
    from invoke import task
    from minchin.text import title, subtitle, query_yes_no, ANSWERS
except ImportError:
    raise ImportError(f"{LOG_PREFIX} Install `invoke` and `minchin.text` to use interactive post creation.")


@task
def new_upost(ctx):
    """
    Interactively create a new micro post.
    """

    # TODO: Allow setting the configuration file from the command line
    try:
        from pelicanconf import CONTENT
    except ImportError:
        CONTENT = "content"

    # try:
    #     from pelicanconf import POST_FOLDER
    # else:
    #     POST_FOLDER = "posts"

    try:
        from pelicanconf import MICROBLOG_FOLDER
    except ImportError:
        from minchin.pelican.readers.microblog.constants import DEFAULT_MICROBLOG_FOLDER as MICROBLOG_FOLDER

    try:
        from pelicanconf import AUTHOR
    except ImportError:
        # import default author from Pelican
        AUTHOR = None

    try:
        from pelicanconf import TZ
    except ImportError:
        TZ = "UTC"


    title(f"Micropost Reader, v{__version__}")
    subtitle("Interactive micropost creator")

    default_folder = Path(CONTENT) / POST_FOLDER / MICROBLOG_FOLDER
    my_folder = input(f"Micropost folder? [{default_folder}] ")
    if my_folder is None:
        my_folder = default_folder

    now = datetime.datetime.now()
    default_fn = "{0:%Y%m%d%H%M}.md".format(now)
    my_fn = input(f"Micropost filename? [{default_fn}] ")
    if my_fn is None:
        my_fn = default_fn

    q_image = text.query_yes_no("Include image?", default="no")
    # add ask for image_fn

    post_body = input("Micropost body: ")

    my_file = Path(my_folder).resolve() / my_fn

    create_file = ANSWERS.YES
    if my_file.exists():
        create_file = query_yes_no(f'File "{my_file}" already exists. Overwrite?', default = "yes")

    if not create_file:
        print("Not creating file. Exiting...")
        sys.exit(1)

    my_file.touch()

    write_body = [
        f"date: {now}",
        f"author: {AUTHOR}" if AUTHOR else "",
        f"image: {image_fn}" if image_fn else "",
        "",
        f"{post_body}",
        "",
    ]
    my_file.write_text("/n".join[write_body])

    print("[GOOD] micropost written!")



