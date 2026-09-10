"""
Structured logging foundation for PrimeProcessing.com.

Rules enforced by this module:
- No secret values (API keys, credentials, tokens) are ever logged.
- Log level is configurable via settings, not hard-coded.
- Log format is consistent across the application.
"""

import logging
import sys

_LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"

# Field names that must never appear with their real value in a log message.
# Later phases (e.g. API Integration) must extend this set rather than
# logging sensitive fields directly.
REDACTED_KEYS = {"api_key", "apikey", "password", "secret", "secret_key", "token", "authorization"}


def redact(data: dict) -> dict:
    """Return a copy of a dict with any sensitive-looking keys masked."""
    return {
        key: ("***REDACTED***" if key.lower() in REDACTED_KEYS else value)
        for key, value in data.items()
    }


def configure_logging(log_level: str = "INFO") -> None:
    """Configure the root logger once for the whole application."""
    root_logger = logging.getLogger()

    if root_logger.handlers:
        root_logger.setLevel(log_level)
        return

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(logging.Formatter(_LOG_FORMAT))

    root_logger.setLevel(log_level)
    root_logger.addHandler(handler)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
