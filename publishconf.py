#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import sys
sys.path.append('.')
from pelicanconf import *

SITEURL = 'http://capitoledulibre.org/2013'

MENUITEMS = (('Programme', SITEURL + '/programme.html'),
             ('Sponsors', SITEURL + '/sponsors.html'),
             ('Informations pratiques', SITEURL + '/informations-pratiques.html'),
             ('Communication', SITEURL + '/communication.html'),
             ('Blog', SITEURL + '/blog.html'),
             ('Videos', SITEURL + '/conferences/'),)

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Uncomment following line for absolute URLs in production:
RELATIVE_URLS = False

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
