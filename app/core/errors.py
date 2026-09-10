"""
Structured error model for PrimeProcessing.com.

Phase 00 establishes the shared error contract only. No business-rule
errors (import, cleaning, extraction, etc.) are defined here — those
belong to the phases that implement those modules.

Design goals:
- Every JSON (API) error response has a consistent, predictable shape.
- Every HTML (page) error shows a themed error page, never a stack trace.
- Error codes are stable strings the frontend JS can branch on, separate
  from human-readable messages that may change.
"""

from flask import jsonify, render_template, request


class AppError(Exception):
    """Base application error carrying an HTTP status and a stable code."""

    def __init__(self, message: str, code: str = "APP_ERROR", status_code: int = 400, details=None):
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code
        self.details = details


def _wants_json() -> bool:
    """Route API requests to a JSON envelope, page requests to an HTML page."""
    return request.path.startswith("/api/") or request.accept_mimetypes.accept_json


def _error_envelope(code: str, message: str, details=None):
    return {"success": False, "error": {"code": code, "message": message, "details": details}}


def register_error_handlers(app) -> None:
    """Register all shared error handlers on the Flask app instance."""

    @app.errorhandler(AppError)
    def handle_app_error(exc: AppError):
        if _wants_json():
            return jsonify(_error_envelope(exc.code, exc.message, exc.details)), exc.status_code
        return (
            render_template("error.html", code=exc.status_code, message=exc.message),
            exc.status_code,
        )

    @app.errorhandler(404)
    def handle_not_found(exc):
        if _wants_json():
            return (
                jsonify(_error_envelope("NOT_FOUND", "The requested resource was not found.")),
                404,
            )
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def handle_server_error(exc):
        # Never expose the real exception message or stack trace to the client.
        app.logger.exception("Unhandled server error")
        if _wants_json():
            return (
                jsonify(
                    _error_envelope(
                        "INTERNAL_SERVER_ERROR", "An unexpected error occurred. Please try again."
                    )
                ),
                500,
            )
        return render_template("error.html", code=500, message="An unexpected error occurred."), 500
