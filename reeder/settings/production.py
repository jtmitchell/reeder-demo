# -*- coding: utf-8 -*-

from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
