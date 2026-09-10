"""Health/readiness endpoint. Confirms the service is up and configured."""

from flask import Blueprint, current_app, jsonify

from app.models.common import HealthStatus, success_envelope

bp = Blueprint("api_health", __name__)

APP_VERSION = "0.0.0-phase00"


@bp.get("/health")
def get_health():
    """Return service health as JSON. Used by frontend JS and deployment checks."""
    settings = current_app.config["PP_SETTINGS"]
    status = HealthStatus(
        status="ok",
        app_name=settings.app_name,
        app_env=settings.app_env,
        version=APP_VERSION,
    )
    return jsonify(success_envelope(data=status.to_dict()))
