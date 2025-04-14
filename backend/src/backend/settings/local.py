# ruff: noqa: F403, F405
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "test": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "test.db",
    },
}
