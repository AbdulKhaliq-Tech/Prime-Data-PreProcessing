# PrimeProcessing.com

An integrated data cleaning, transformation, analysis, visualization, and
conversion platform. Users import data (CSV, Excel, JSON, XML, HTML),
process it through a shared in-memory dataset, and export or convert the
results — all through one consistent, single-Python web application.

> **Project separation note:** PrimeProcessing.com is a separate project
> from the EDA AI Assistant. No EDA-specific pages, AI-generated insights,
> chatbot behavior, or machine-learning features belong in this project.

## Current Development Status

**Phase 00 — Project Foundation & Development Environment: READY FOR REVIEW**

The repository has a working, pure-Python (Flask) foundation with no
functional data-processing modules active yet. See
[`docs/phases/phase-00-completion-report.md`](docs/phases/phase-00-completion-report.md)
for full implementation and test details.

## 13-Phase Roadmap

| Phase | Scope | FR | Status |
|---|---|---|---|
| 00 | Foundation & Development Environment | — | READY FOR REVIEW |
| 01 | Landing Page, Application Shell, Settings & Shared Data Preview | — | NOT STARTED |
| 02 | Import Parser / File Ingestion | FR-01 | NOT STARTED |
| 03 | Data Cleaning | FR-02 | NOT STARTED |
| 04 | Data Customization | FR-03 | NOT STARTED |
| 05 | Data Extraction | FR-04 | NOT STARTED |
| 06 | Statistical Analysis | FR-06 | NOT STARTED |
| 07 | Visualization | FR-05 | NOT STARTED |
| 08 | File Conversion | FR-07 | NOT STARTED |
| 09 | Data Export | FR-12 | NOT STARTED |
| 10 | Mock Data Generation | FR-09 | NOT STARTED |
| 11 | Automation Engine | FR-10 | NOT STARTED |
| 12 | API Integration + Word Report Generator + Final Integration | FR-11 + FR-08 | NOT STARTED (Word Report Generator is deferred until this phase) |

*FR numbers use the SRS's own numbering (adopted as canonical for this
project — see [`docs/architecture/overview.md`](docs/architecture/overview.md)
for the correction record).*

## Core SRS-Supported Capabilities (platform-wide, delivered across phases)

- Multi-format data import and export (CSV, Excel, JSON, XML, HTML)
- Data cleaning (missing values, formatting, standardization)
- Data customization (merge, split, filter, sort, pivot)
- Data extraction (emails, URLs, phone numbers, text patterns)
- Statistical analysis (20 measures) and data-aware visualization
- File conversion, mock data generation, automation, API integration
- Word Report Generator (deferred until Phase 12)

## What's Implemented in Phase 00

- **A single Flask application** — no separate frontend build, no
  Node.js/npm, matching the SRS's Python-only stack.
- Environment-validated configuration, structured error handling (JSON
  for API routes, themed HTML pages for browser routes), structured
  logging, and a `/api/health` endpoint.
- A four-theme CSS design-token system (Arctic Blue, Warm Pearl, Midnight
  Blue, Graphite) applied via a `data-theme` attribute, switchable and
  persisted client-side.
- Reusable UI primitives as Jinja macros (Button, Input, Select, Card,
  Dialog, Tooltip, Status, Loading, Empty/Error states).
- A small vanilla-JS API-client boundary for future AJAX calls.
- Future DataFrame-processing contracts (interfaces only, no logic).
- A pytest-based testing foundation — 18 tests, all passing.

Nothing beyond the foundation is active: no import, cleaning,
transformation, extraction, visualization, statistics, conversion, mock
data, automation, API integration, export, or Word Report Generator
functionality exists yet.

## Technology / Environment

- **Language/Framework:** Python 3.11+, Flask.
- **Templating/Styling:** Jinja2, plain CSS (no framework), vanilla JS.
- **Testing:** pytest.
- **Data libraries (installed now for later phases):** pandas, numpy,
  matplotlib, plotly, openpyxl, python-docx, requests, Faker.
- **Data layer:** In-memory only (no database), per the SRS architecture.

## Installation and Run Instructions

See [`docs/development/setup.md`](docs/development/setup.md) for full
step-by-step instructions. Quick start:

```bash
pip install -r requirements.txt
cp .env.example .env
python run.py
```

Then open `http://localhost:8000/`.

## Dependencies / Configuration

- Config: `.env.example` (copy to `.env`). Required: `SECRET_KEY`,
  `APP_ENV`, `PORT`, `LOG_LEVEL`.
- No real secrets are committed anywhere in this repository.

## Testing / Verification

```bash
python -m pytest -v
```

All 18 tests currently pass — see the Phase 00 completion report for
exact results, including live-server verification.

## Known Limitations

- No functional data-processing module exists yet (by design — Phase 00
  is foundation-only).

## Deferred Functionality

- Word Report Generator (FR-08) — explicitly deferred until Phase 12.
- Complete Landing Page content, full Settings screen, and the complete
  Data Preview table — Phase 01.

## Next Authorized Phase

**Phase 01 — Landing Page, Application Shell, Settings & Shared Data
Preview**, pending project-owner review and confirmation of Phase 00.
