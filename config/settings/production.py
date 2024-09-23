# ruff: noqa: F403,F405
import dj_database_url

from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

# Parse database configuration from $DATABASE_URL
DATABASES["default"] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# static files served from Amazon S3
AWS_STORAGE_BUCKET_NAME = get_env_variable("AWS_STORAGE_BUCKET_NAME")
AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY")
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto.S3BotoStorage",
    },
}
S3_URL = f"http://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/"
STATIC_URL = S3_URL
