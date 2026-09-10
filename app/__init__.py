"""
PrimeProcessing.com application factory.

Phase 00 scope only: app wiring, configuration, structured error handling,
structured logging, health/readiness endpoint, template context (themes),
and the landing route. No functional data-processing endpoints exist yet.
"""

from flask import Flask

from app.core.config import Settings, load_settings
from app.core.errors import register_error_handlers
from app.core.logging import configure_logging, get_logger
from app.state.themes import THEMES


def create_app(settings: Settings | None = None) -> Flask:
    """Application factory. Keeps startup validation and wiring in one place."""
    # Fails fast if required configuration is missing/invalid.
    settings = settings or load_settings()

    configure_logging(settings.log_level)
    logger = get_logger(__name__)
    logger.info(
        "Starting %s in '%s' mode (debug=%s)",
        settings.app_name,
        settings.app_env,
        settings.app_debug,
    )

    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config["PP_SETTINGS"] = settings
    app.config["SECRET_KEY"] = settings.secret_key
    app.config["DEBUG"] = settings.app_debug

    register_error_handlers(app)

    from app.api.health import bp as health_bp
    from app.routes.main import bp as main_bp

    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(main_bp)

    @app.context_processor
    def inject_shared_template_context():
        """Make theme list and app identity available to every template."""
        return {"app_name": settings.app_name, "themes": THEMES}

    return app
