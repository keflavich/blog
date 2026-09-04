#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = u'Adam Ginsburg'
SITENAME = u"Adam Ginsburg's blog"
#SITESUBTITLE = u"about astronomy and coding, most likely"
#SITEURL = 'file://localhost/Volumes/disk5/Users/adam/repos/blog/output'
#SITEURL = ""
SITEURL = 'https://keflavich.github.io/blog'

TIMEZONE = 'America/Denver'
PATH = "content/"

DEFAULT_LANG = u'en'

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)
LINKS=()

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL=()

DEFAULT_PAGINATION = 10

# The theme is vendored in this repo at ./mine -- no external checkout or
# `pelican-themes --install` step is required. Edit it in place and commit.
THEME = './mine'

STATIC_PATHS = ['images','bgps/images','iau303/images','images/sgrb2']

INLINESTYLES = True

#DISQUS_SITENAME = "keflavich-pelican"
#DISQUS_SITENAME = "adamginsburgsblog"

BGIMAGE='images/GC_4096sq_bolo.png'

DISPLAY_PAGES_ON_MENU = False
SUPPRESS_CATEGORIES_ON_MENU = True
SHOW_TAGS=False
SHOW_SIDEBAR=True
SHOW_RECENT=True

DATE_FORMATS = {'en':"%Y/%m/%d"}

MENUITEMS = [('Homepage','https://www.adamgginsburg.com',),
             ('Blog Index','/index.html',),
             ('BGPS Blog','/category/bgps.html',),
             ('Publications','/category/publications.html',),
             ('Archives','/archives.html',),
             ('Tags','/tags.html',),
            ]

PLUGIN_PATHS = []#os.path.expanduser('~/repos/pelican-plugins')]
PLUGINS = ["render_math"]

USE_FOLDER_AS_CATEGORY = True

# Recent docutils releases enforce a per-line length limit (default 10000)
# that rejects a few older posts containing very long lines (e.g. embedded
# data/tables). Raise it so the historical content keeps building unchanged.
DOCUTILS_SETTINGS = {'line_length_limit': 1000000}

DISQUS_SITENAME = "adamginsburgsblog"
GOOGLE_ANALYTICS = 'UA-37306139-1'

# links just don't work in pelican, do they?
#RELATIVE_URLS = False
