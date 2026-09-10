"""
Route/template smoke tests — Phase 00 foundation testing requirement.

Confirms the app shell, theming, and template/macro system render without
error. No functional module content is asserted here (none exists yet).
"""


def test_landing_page_renders(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"PrimeProcessing.com" in response.data
    assert b"Project foundation ready" in response.data


def test_landing_page_includes_all_four_themes(client):
    response = client.get("/")
    body = response.data.decode("utf-8")
    for theme_id, label in [
        ("arctic-blue", "Arctic Blue"),
        ("warm-pearl", "Warm Pearl"),
        ("midnight-blue", "Midnight Blue"),
        ("graphite", "Graphite"),
    ]:
        assert f'value="{theme_id}"' in body
        assert label in body


def test_landing_page_links_all_theme_stylesheets(client):
    response = client.get("/")
    body = response.data.decode("utf-8")
    for filename in [
        "css/tokens.css",
        "css/themes/arctic-blue.css",
        "css/themes/warm-pearl.css",
        "css/themes/midnight-blue.css",
        "css/themes/graphite.css",
        "css/global.css",
        "css/shell.css",
    ]:
        assert filename in body


def test_static_theme_css_files_are_served(client):
    for filename in [
        "css/themes/arctic-blue.css",
        "css/themes/warm-pearl.css",
        "css/themes/midnight-blue.css",
        "css/themes/graphite.css",
    ]:
        response = client.get(f"/static/{filename}")
        assert response.status_code == 200
