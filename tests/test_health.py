"""Startup/health test — Phase 00 foundation testing requirement."""


def test_app_starts(app):
    """The app must start (settings validation must have passed already)."""
    assert app is not None


def test_health_endpoint_returns_ok(client):
    response = client.get("/api/health")
    assert response.status_code == 200

    body = response.get_json()
    assert body["success"] is True
    assert body["data"]["status"] == "ok"
    assert body["data"]["app_name"] == "PrimeProcessing.com"
    assert "timestamp" in body["data"]


def test_unknown_api_route_returns_standard_json_error_envelope(client):
    response = client.get("/api/does-not-exist")
    assert response.status_code == 404

    body = response.get_json()
    assert body["success"] is False
    assert body["error"]["code"] == "NOT_FOUND"


def test_unknown_page_route_returns_404_html(client):
    response = client.get("/does-not-exist", headers={"Accept": "text/html"})
    assert response.status_code == 404
    assert b"Page not found" in response.data
