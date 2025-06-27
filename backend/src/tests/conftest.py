import os

import django
import pytest
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings.local")
django.setup()


@pytest.fixture(scope="session", autouse=True)
def print_database_info() -> None:
    """
    Fixture to print the current database information before running tests.
    """
    print(f"Using database: {settings.DATABASES["default"]}")


@pytest.fixture(scope="session")
def django_db_setup() -> None:
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",  # Or a file path if not using in-memory
        "ATOMIC_REQUESTS": True,
    }
