"""
PrimeProcessing.com — development entry point.

Usage:
    python run.py
"""

from app import create_app
from app.core.config import load_settings

settings = load_settings()
app = create_app(settings=settings)

if __name__ == "__main__":
    app.run(host=settings.host, port=settings.port, debug=settings.app_debug)
