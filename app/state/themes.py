"""
Theme metadata for PrimeProcessing.com's four approved application themes.

This is the single source of truth the templates use to render the theme
selector. The actual visual definition of each theme lives in
static/css/themes/*.css, keyed by the same `id` values used here.
"""

THEMES = [
    {"id": "arctic-blue", "label": "Arctic Blue", "mode": "light"},
    {"id": "warm-pearl", "label": "Warm Pearl", "mode": "light"},
    {"id": "midnight-blue", "label": "Midnight Blue", "mode": "dark"},
    {"id": "graphite", "label": "Graphite", "mode": "dark"},
]

DEFAULT_THEME_ID = "arctic-blue"
