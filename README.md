reeder-demo
===========

Simple django site for a Juju demo

## 16 July 2014

This code has been adapted into a 12 Factor App style,
and had a RESTish API added using *Restless*

## Installation

You will need a Postgresql database to connect to, and have setup login details.

1. Checkout this git repository
2. `pip install -r requirements/development.txt`
2. Setup environment variables for
* `REEDER_DB_USER`
* `REEDER_DB_PASSWORD`
* `DJANGO_SETTINGS_MODULE=reeder.settings.development`

Optionally you can use `foreman` to start the app, with the supplied Procfile
and put the enviroment settings into a `.env` file.
