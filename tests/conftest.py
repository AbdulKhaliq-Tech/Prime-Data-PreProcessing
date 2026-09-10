import pytest

from app import create_app
from app.core.config import load_settings


@pytest.fixture()
def settings():
    return load_settings(
        env={
            "APP_NAME": "PrimeProcessing.com",
            "APP_ENV": "test",
            "APP_DEBUG": "false",
            "SECRET_KEY": "test-secret-key",
            "HOST": "0.0.0.0",
            "PORT": "8000",
            "LOG_LEVEL": "INFO",
            "MAX_UPLOAD_SIZE_MB": "50",
        }
    )


@pytest.fixture()
def app(settings):
    flask_app = create_app(settings=settings)
    flask_app.config.update(TESTING=True)
    return flask_app


@pytest.fixture()
def client(app):
    return app.test_client()
