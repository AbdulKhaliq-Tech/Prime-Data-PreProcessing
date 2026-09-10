"""Configuration validation test — Phase 00 foundation testing requirement."""

import pytest

from app.core.config import ConfigurationError, load_settings

VALID_ENV = {
    "APP_NAME": "PrimeProcessing.com",
    "APP_ENV": "development",
    "APP_DEBUG": "true",
    "SECRET_KEY": "test-secret-key",
    "HOST": "0.0.0.0",
    "PORT": "8000",
    "LOG_LEVEL": "INFO",
    "MAX_UPLOAD_SIZE_MB": "50",
}


def _env(**overrides):
    merged = dict(VALID_ENV)
    merged.update(overrides)
    return merged


def test_valid_settings_load_successfully():
    settings = load_settings(env=_env())
    assert settings.app_name == "PrimeProcessing.com"
    assert settings.app_env == "development"
    assert 1 <= settings.port <= 65535


def test_invalid_app_env_is_rejected():
    with pytest.raises(ConfigurationError):
        load_settings(env=_env(APP_ENV="not-a-real-environment"))


def test_invalid_port_is_rejected():
    with pytest.raises(ConfigurationError):
        load_settings(env=_env(PORT="not-a-number"))


def test_port_out_of_range_is_rejected():
    with pytest.raises(ConfigurationError):
        load_settings(env=_env(PORT="0"))


def test_invalid_log_level_is_rejected():
    with pytest.raises(ConfigurationError):
        load_settings(env=_env(LOG_LEVEL="NOT_A_LEVEL"))


def test_missing_secret_key_is_rejected():
    with pytest.raises(ConfigurationError):
        load_settings(env=_env(SECRET_KEY=""))


def test_invalid_max_upload_size_is_rejected():
    with pytest.raises(ConfigurationError):
        load_settings(env=_env(MAX_UPLOAD_SIZE_MB="-5"))
