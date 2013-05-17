#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Adam Ginsburg'
SITENAME = u"Adam Ginsburg's blog"
#SITESUBTITLE = u"about astronomy and coding, most likely"
SITEURL = 'http://keflavich.github.com/blog/'

TIMEZONE = 'America/Denver'

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

#THEME='bootstrap2' # sneakyidea is default
THEME='mine'
THEME='waterspill-en' 
THEME='simple_editable' 
 
STATIC_PATHS = ['images']

INLINESTYLES = True

DISQUS_SITENAME = "keflavich-pelican"

BGIMAGE='images/GC_4096sq_bolo.png'

DISPLAY_PAGES_ON_MENU = False
SUPPRESS_CATEGORIES_ON_MENU = True
SHOW_TAGS=False
SHOW_RECENT=True

MENUITEMS = {'Home':'http://www.adamgginsburg.com','Index':'index.html'}.items()

#PLUGINS = ["latex"]

