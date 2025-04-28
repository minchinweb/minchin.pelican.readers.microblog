"""
Supporting invoke tasks.
"""

from pathlib import Path

from minchin.pelican.readers.microblog import __version__
from minchin.pelican.readers.microblog.constants import LOG_PREFIX


try:
    from invoke import task
    import minchin.text as text
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


    text.title(f"Micropost Reader, v{__version__}")
    text.subtitle("Interactive micropost creator")

    default_folder = Path(CONTENT) / POST_FOLDER / MICROBLOG_FOLDER
    my_folder = input(f"Micropost folder? [{default_folder}] ")
    if my_folder is None:
        my_folder = default_folder




