# ruff: noqa: F403, F405
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS: list[str] = ["*"]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

print("Using production database settings")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db" / "db.sqlite3",
    },
}
