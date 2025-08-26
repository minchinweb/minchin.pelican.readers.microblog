=====================
Pelican Microblogging
=====================

*A Pelican plugin providing "microblogging" capabilities.*

.. image:: https://img.shields.io/pypi/v/minchin.pelican.readers.microblog.svg?style=flat
   :target: https://pypi.python.org/pypi/minchin.pelican.readers.microblog/
   :alt: PyPI version number

.. image:: https://img.shields.io/badge/-Changelog-success
   :target: https://github.com/MinchinWeb/minchin.pelican.readers.microblog/blob/master/CHANGELOG.rst
   :alt: Changelog

.. image:: https://img.shields.io/pypi/pyversions/minchin.pelican.readers.microblog?style=flat
   :target: https://pypi.python.org/pypi/minchin.pelican.readers.microblog/
   :alt: Supported Python version

.. image:: https://img.shields.io/pypi/l/minchin.pelican.readers.microblog.svg?style=flat&color=green
   :target: https://github.com/MinchinWeb/minchin.pelican.readers.microblog/blob/master/LICENSE.txt
   :alt: License

.. image:: https://img.shields.io/pypi/dm/minchin.pelican.readers.microblog.svg?style=flat
   :target: https://pypi.python.org/pypi/minchin.pelican.readers.microblog/
   :alt: Download Count

Quickstart
----------

1. Install the plugin via pip: ``pip install minchin.pelican.readers.microblog``
2. Generally, the plugin should be loaded and configured automatically without
   further effort on your part.
3. Create a ``micro`` folder in your content folder (to hold your micro blog
   posts!).
4. Create a new post in your ``micro`` folder. This can be generally be just
   the text (body) of your post. In terms of metadata, ``title`` is unneeded
   (and ignored), ``slug`` will be auto-generated (based on the post date), and
   ``date`` will determined from the file creation datetime of the post file.
   If you provide the ``date``, it must be on the first line, in ``key: value``
   format. The text body will be read as Markdown (so plain text effectively
   works too)!
5. Regenerate your Pelican site!

Sample (Micro) Post File
------------------------

.. code-block:: md

   <!-- ./content/micro/202307091701.md -->

   date: 2023-07-09 17:01

   I'm microblogging with Pelican!
   https://blog.minchin.ca/label/microblogging-pelican

Or a post with an image:

.. code-block:: md

   <!-- ./content/micro/202307112138.md -->

   date: 2023-07-11 21:38
   image: images/birger-strahl-olI66vtMgNo-unsplash.jpg

   Microblog posts can have "feature" images too! (URL of photo should
   automatically be added.)

The image path is relative to your ``content`` folder. A URL of the photo is
added to the end of the post as well.

Or with tags (or hashtags):

.. code-block:: md

   <!-- ./content/micro/202307131456.md -->

   date: 2023-07-13 14:56
   tags: Python, Pelican, Microblogging

   I'm now Microblogging with Pelican!


This will add links at the end of your post to the tags to the tag page for
your (Pelican) site.

For now, it does not pull tags out of the body of your post.

Background Notes (on Micro Blogging)
------------------------------------

Microblogging is here considered to be blog posts, but very short in length.

The most common example is Twitter, with an original limit of 140 characters
(to be less than the SMS max of 160 characters). Twitter has since doubled
their limit to 280 characters. The default on Mastodon is 500 characters, the
same as (newly released) Threads. (Note that on Twitter, all links are run
through a shortener and so are considered 23 characters long.) Here, the
default soft limit is 140 characters. You can choose to ignore that, or set a
higher limit (via ``MICROBLOG_MAX_LENGTH``), but there are certain assumptions
about presentation that start to fail as the posts get longer....

Installation
------------

The easiest way to installed *Microblogging* is through ``pip``:

.. code-block:: sh

   pip install minchin.pelican.reader.microblog

Requirements
------------

*Microblogging* relies on Pelican, and the ``autoloader`` plugin (for
autoloading). If this plugin is installed from PyPI, these should automatically
be installed.

If you need to insrall them manually:

.. code-block:: sh

   pip install pelican
   pip install minchin.pelican.plugins.autoloader

..
    Additional Images
    -----------------

    Micro blog post, using the Seafoam theme:

    (Placeholder image for the moment...)

    .. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.6.0/article_with_header.png
    :align: center
    :alt: Replace Image...


Pelican Settings
----------------

These settings can be set in your ``pelicanconf.py`` file (your Pelican settings
file) to alter the behavior of the plugin.

If a value is given below, this represents the effective default value. If no
value is given, the effective default value is ``None``.

*Microblogging* also auto-configures itself when possible.  If you need to
manually create the default configuration, you would need the following:

.. code-block:: python

   # pelicanconf.py

   # if PLUGINS is not defined on Pelican 4.5+, these plugins will autoload
   PLUGINS = [
       "minchin.pelican.readers.microblog",
       # others, as desired...
   ]

   # the rest of the your configuration file...

This documentation has to be manually updated. If the settings no longer match
the plugin's behavior, or a setting is missing from here, please open a ticket
on `GitHub
<https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues>`_.

.. use the ".. data::" directive here for Sphinx output, but on GitHub, that just causes everything to disappear

ARTICLE_ORDER_BY = "reverse-date"
   Sorting order for micro blog posts (also used for sorting posts generally);
   micro posts will be sorted among all posts. (Regular Pelican setting)
AUTHOR
    Default author for micro blog posts. Can be overwritten by the metadata at
    the top of individual posts. (Regular Pelican setting; you don't have to
    supply an author.)
MICROBLOG_APPEND_HASHTAGS = True
   Tags gets appended at the end of the micro blog post as hashtags.
   *#taggedyou*  Tags have the CSS class ``.microblog-post-tag`` applied, if
   you want to conditionally control their display or formatting.
MICROBLOG_CATEGORY = "µ"
   Default category for your micro blog posts. It could be overwritten by the
   metadata on top of individual posts.
   
   Note that Pelican will render the slug (used in URLs) for this default as
   ``m``.
MICROBLOG_FOLDER = "micro"
   Folder containing your micro blog posts, relative to your content root
   folder.
MICROBLOG_MAX_LENGTH = 140
   How long should your micro blog posts be limited to. Pelican will emit a
   warning if you exceed this.
MICROBLOG_SAVE_AS = ARTICLE_SAVE_AS
   What to save the micro blog posts output file as. Defaults to using the same
   file structure as you are using for articles (aka "regular" posts). c.f.
   ``MICROBLOG_URL``.
MICROBLOG_SLUG = "u{date:%Y%m%d%H%M}"
   The slug that will be used for micro blog posts. Eg. ``u202307091701``.

   Note that Pelican expects slugs to be universally unique.
MICROBLOG_URL = ARTICLE_URL
   What URL to post the micro blog posts to. Defaults to using the same URL
   structure as you are using for articles (aka "regular" posts). c.f.
   ``MICROBLOG_SAVE_AS``.

Integration with Themes
-----------------------

For best support, you will need to modify your theme, or select a theme that
already supports *Microblogging*, like my `Seafoam
<http://blog.minchin.ca/label/seafoam/>`_.

Some helpful notes:

- Microblog posts are considered ``Articles`` by Pelican, and will be included
  in the ``articles`` and ``dates`` "lists" provided by the templating engine.
- Microblog posts all have ``article.micro = True``.
- Microblog posts are added to the ``µ`` category (by default).
- Generally, you'll want to disregard and not show the title of the microblog
  post. The title is set to the slug.
- Because of their short length, it may make sense to display the whole body
  (``article.content``) in places that a link via the title of the article is
  typically shown.
- Appended tags have the CSS class ``.microblog-post-tag`` applied.
- Appended links to featured images have the CSS class
  ``.microblog-post-image`` applied.

Changelog
---------

`Changelog <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/blob/master/CHANGELOG.rst>`_

Roadmap
-------

These are features that I would like to eventually add to the plugin (and the
issues I'm using to track their progress):

- `Issue 1
  <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues/1>`_
  -- count links as 23 characters (*à la* Twitter)
- `Issue 2
  <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues/2>`_
  -- process ReST microblog posts
- `Issue 3
  <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues/3>`_
  -- CLI command to create microposts
- `Issue 4
  <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues/4>`_
  -- add link previews
- `Issue 5
  <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues/5>`_
  -- show (if applicable) that this is a reply to something (or a "re-tweet")
- `Issue 6
  <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues/6>`_
  -- show replies to each post (borrow the comment setup?)
- `Issue 7
  <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues/7>`_
  -- automatically add hashtags as (Pelican) tags

Pull Requests to implement any of these are welcomed!

Known Issues
------------

- Processing relies on Pelican's built-in Markdown reader.
- The length of links to featured images will change if the ``SITE_URL``
  changes. This can mean that the microblog post is "short" enough when
  reviewing your site locally, but not when the site is generated for
  publication.
- linking to internal content from microposts (i.e.
  `{filename}../regular-post.md`) crashes Pelican -- `Issue 9
  <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues/9>`_
- relies on `str.removesuffix()`, which means this only supports Python 3.9 or
  better.

.. Credits
