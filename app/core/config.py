"""
Centralized environment/configuration loading for PrimeProcessing.com.

Phase 00 scope:
- Load and validate configuration required for the foundation (app
  identity, server binding, secret key, logging, and a placeholder
  upload-size limit for future phases).
- Fail fast at startup if required configuration is missing or invalid.
- Never log secret values.

This module intentionally contains no business/data-processing logic.
Kept as plain Python (no third-party validation library) to match the
SRS's lean Python + Flask stack.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

ALLOWED_APP_ENVS = {"development", "test", "staging", "production"}
ALLOWED_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


class ConfigurationError(Exception):
    """Raised when required configuration is missing or invalid at startup."""


@dataclass(frozen=True)
class Settings:
    app_name: str
    app_env: str
    app_debug: bool
    secret_key: str
    host: str
    port: int
    log_level: str
    max_upload_size_mb: int


def _to_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}


def load_settings(env: dict | None = None) -> Settings:
    """
    Build and validate a Settings instance from environment variables.

    `env` may be supplied for testing; defaults to the real process
    environment (after loading a local .env file, if present).
    """
    load_dotenv(override=False)
    source = env if env is not None else os.environ

    app_env = source.get("APP_ENV", "development")
    if app_env not in ALLOWED_APP_ENVS:
        raise ConfigurationError(
            f"APP_ENV must be one of {sorted(ALLOWED_APP_ENVS)}, got '{app_env}'"
        )

    log_level = source.get("LOG_LEVEL", "INFO").upper()
    if log_level not in ALLOWED_LOG_LEVELS:
        raise ConfigurationError(
            f"LOG_LEVEL must be one of {sorted(ALLOWED_LOG_LEVELS)}, got '{log_level}'"
        )

    port_raw = source.get("PORT", "8000")
    try:
        port = int(port_raw)
    except ValueError as exc:
        raise ConfigurationError(f"PORT must be an integer, got '{port_raw}'") from exc
    if not (1 <= port <= 65535):
        raise ConfigurationError(f"PORT must be between 1 and 65535, got {port}")

    max_upload_raw = source.get("MAX_UPLOAD_SIZE_MB", "50")
    try:
        max_upload_size_mb = int(max_upload_raw)
    except ValueError as exc:
        raise ConfigurationError(
            f"MAX_UPLOAD_SIZE_MB must be an integer, got '{max_upload_raw}'"
        ) from exc
    if max_upload_size_mb <= 0:
        raise ConfigurationError("MAX_UPLOAD_SIZE_MB must be a positive integer")

    secret_key = source.get("SECRET_KEY", "")
    if not secret_key:
        raise ConfigurationError("SECRET_KEY is required and must not be empty")

    return Settings(
        app_name=source.get("APP_NAME", "PrimeProcessing.com"),
        app_env=app_env,
        app_debug=_to_bool(source.get("APP_DEBUG", "true")),
        secret_key=secret_key,
        host=source.get("HOST", "0.0.0.0"),
        port=port,
        log_level=log_level,
        max_upload_size_mb=max_upload_size_mb,
    )
