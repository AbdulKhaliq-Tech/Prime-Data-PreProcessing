"""
Shared JSON response conventions for PrimeProcessing.com.

Phase 00 defines the envelope shape only. Endpoint-specific payloads are
introduced by the phases that own that functionality.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Optional


def success_envelope(data: Any = None, message: Optional[str] = None) -> dict:
    """Standard success envelope for JSON API responses."""
    return {"success": True, "data": data, "message": message}


@dataclass
class HealthStatus:
    """Payload returned by the health/readiness endpoint."""

    status: str
    app_name: str
    app_env: str
    version: str
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "status": self.status,
            "app_name": self.app_name,
            "app_env": self.app_env,
            "version": self.version,
            "timestamp": self.timestamp,
        }
