# -*- coding: utf-8 -*-
# override settings for the environment

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'reeder',                      # Or path to database file if using sqlite3.
        'USER': 'wrappz',                      # Not used with sqlite3.
        'PASSWORD': 'wrappz',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
