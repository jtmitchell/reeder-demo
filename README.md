# Reeder RSS Demo

Simple demo django site.

## Installation

You will need a Postgresql database to connect to, and have setup login details.

The tooling is using [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just).

1. Install ``uv`` and ``just`` if you don't have them.
1. Checkout this git repository
1. `just install`
1. Setup environment variables for
* `REEDER_DB_USER`
* `REEDER_DB_PASSWORD`
* `DJANGO_SETTINGS_MODULE=config.settings.development`
* `DJANGO_SECRET_KEY=`<some secret key>
