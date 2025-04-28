Changelog
=========

.. Added, Changed, Depreciated, Removed, Fixed, Security

.. this is in "release" (for Sphinx) format

- :release:`1.3.0 <2024-10-01>`
- :bug:`- major` Ignore appended (hash)tags and featured image links in
  determining post length. C.f. `Issue #1
  <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues/1>`_.
- :bug:`10 major` Rework creation of featured image links so the link is
  actually valid.
- :bug:`- major` Apply CSS class (of ``.microblog-post-image``) to appended
  featured image links. Thus, conditional display of them is possible.
- :bug:`- major` Apply CSS class (of ``.microblog-post-tag``) to appended tags.
  Thus, conditional display of them is possible.
- :feature:`13` Set ``ARTICLE_ORDER_BY`` (a default Pelican setting) to control
  micropost sort order. Makes microposts sort as expected. C.f. `Issue #8
  <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues/8>`_.

- :release:`1.2.0 <2024-07-09>`
- :feature:`11` Allow turning off adding tags as hashtags at the end of the
  micropost (see ``MICROBLOG_APPEND_HASHTAGS`` setting).
- :feature:`11` Allow setting micropost category through post metadata.
- :feature:`11` Allow setting micropost author through post metadata. Defaults
  to Pelican setting ``AUTHOR``. (Neither is required to be set.)
- :support:`-` N.b. that the minimum support version of Python is 3.9.

- :release:`1.1.0 <2023-07-13>`
- :feature:`7` Support hashtags, if given in frontend post metadata.

- :release:`1.0.0 <2023-07-11>`
- :support:`-` `seafoam <https://blog.minchin.ca/label/seafoam/>`_ v2.9.0 is
  being release co-currently with this, and has support for microblog posts.
- :feature:`-` Support feature image for microblog posts.
- :feature:`-` Supports basic posting and processing of "micro" blog posts.
  Posts are assumed to be written in Markdown (so plain text works as well).
  Posts must have a ``date`` metadata key.
- :support:`-` Initial release!
