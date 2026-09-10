# Development Setup

## Prerequisites

- Python 3.11+
- Git

No Node.js/npm is required — PrimeProcessing.com is a single Python
(Flask) application.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # edit values as needed for your machine
```

## Run the app

```bash
python run.py
```

Or use the convenience script, which creates `.env` from the example if
it's missing and then starts the server:

```bash
./scripts/dev.sh
```

- App: `http://localhost:8000/`
- Health check (JSON): `http://localhost:8000/api/health`

## Linting and formatting (optional, dev-only)

```bash
pip install -r requirements-dev.txt
python -m black app tests run.py     # auto-format
python -m flake8 app tests run.py    # lint
```

Configuration lives in `pyproject.toml` (black) and `.flake8` (flake8).
Both currently pass clean against the full codebase.

## Run tests

```bash
python -m pytest -v
```

## Project structure

```
app/
  __init__.py     application factory (create_app)
  core/           config loading, logging, error handling
  api/            JSON API blueprints (health, and future FR endpoints)
  routes/         page-view blueprints (landing page, and future module pages)
  models/         shared response/data shapes
  services/       future business-logic services (empty in Phase 00)
  processing/     future DataFrame-processing contracts (interfaces only)
  state/          shared metadata (e.g. the four-theme registry)
  utils/          small shared helpers

templates/
  base.html       application shell (top bar, nav, canvas, status region)
  landing.html    Phase 00 foundation landing content
  404.html        themed not-found page
  error.html      themed generic error page
  macros/ui.html  reusable UI primitives (Button, Input, Select, Card, ...)

static/
  css/
    tokens.css            structural design tokens
    themes/*.css          the four approved themes
    components/*.css      primitive component styles
    global.css, shell.css base + app-shell styles
  js/
    theme.js       theme switching + persistence
    apiClient.js    API-client boundary (fetch wrapper)
    motion.js       reduced-motion helper
    app.js          page bootstrap (health-check wiring)

tests/            pytest suite (config, health, contracts, routes)
docs/             architecture, development, and phase documentation
scripts/dev.sh    convenience script: creates .env if missing, runs the app
run.py            development entry point
pyproject.toml    black configuration
.flake8           flake8 configuration
requirements.txt       runtime dependencies
requirements-dev.txt   + black, flake8 (dev-only)
```

## Scope reminder

This repository currently implements **Phase 00 only** — the project
foundation. No data import, cleaning, transformation, extraction,
visualization, statistical analysis, conversion, mock data generation,
automation, API integration, export, or Word Report Generator
functionality exists yet. See
`docs/phases/phase-00-completion-report.md` for what was actually built
and tested.
