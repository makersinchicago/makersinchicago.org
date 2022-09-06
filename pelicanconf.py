#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import glob

AUTHOR = 'MakersinChicago'
SITENAME = 'Makers in Chicago'
SITEURL = ''

PATH = 'content'
THEME = 'style400'

TIMEZONE = 'US/Central'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

DEFAULT_DATE = (2019, 6, 17, 14, 1, 1)


# Blogroll
LINKS = (
         ('Blog', '/category/blog'),
         ('Map', '/pages/map'),
         ('Twitter', 'https://twitter.com/makersinchicago'),
        #  ('Slack', 'http://bit.ly/chicagomakers-slack'),
         ('Contact','mailto:makersinchicago@jorgegarcia.io?subject=MakersinChicago.org:%20')
        #  ('About', '/pages/about'),
        #  ,
         )

SOCIAL = (('GitHub', 'http://github.com/standage'),
          ('Twitter', 'https://twitter.com/byuhobbes'),
          ('StackExchange', 'http://stackexchange.com/users/208980/daniel-standage?tab=accounts'))
GITHUB_URL = 'http://github.com/makersinchicago'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
