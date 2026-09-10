"""
Main page-view blueprint.

Phase 00 scope: a single foundation landing route proving the app shell,
theming, and template/macro system render correctly. The complete Landing
Page (value statement, capability grid, processing-flow visual, CTA) and
every functional module page (Import, Cleaning, ...) belong to later
phases and are intentionally absent here.
"""

from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    return render_template("landing.html")
