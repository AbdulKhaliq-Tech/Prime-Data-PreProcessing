# PrimeProcessing.com — Architecture Overview

## Authority hierarchy

1. **Complete SRS** — functional authority (what the product must do).
2. **Master UI Guidelines** — visual/interaction authority (how it looks and behaves).
3. **Master Context** — permanent architecture, scope, and process rules.
4. **Active Phase Guide** — the only currently-authorized implementation boundary.
5. **Actual repository** — implementation reality, inspected before every change.

## Architectural style

A **single Python application** built on **Flask**, per the SRS's own
software requirements ("User Interface: A graphical or web-based interface
developed using Flask or Streamlit"; "Programming Language: Python 3.x").
There is no separate frontend build process, no Node.js/npm dependency,
and no second language — HTML is server-rendered via Jinja templates,
styled with plain CSS, and given light interactivity with vanilla
JavaScript (theme switching, health-check polling). This directly matches
the SRS's Development Tools list (VS Code/PyCharm, Git, GitHub — no JS
toolchain) and Deliverables section (single "Functional Software
Application" with a "graphical or web-based interface developed using
Flask or Streamlit").

> **Architecture decision record:** An earlier draft of this foundation
> used a decoupled React + FastAPI stack, inferred from the Master UI
> Guidelines' interaction complexity. The project owner corrected this:
> the SRS explicitly calls for a Python-only stack, and of the two named
> options (Flask or Streamlit) the owner chose **Flask**, for full control
> over the elaborate four-theme/animation/drag-and-drop UI that Streamlit's
> component model cannot express as precisely. This repository was
> rebuilt from scratch on that basis.

## High-level layers (per the SRS), mapped onto the Flask app

- **Presentation Layer** — Jinja templates (`templates/`) rendered by
  Flask view routes (`app/routes/`), styled by `static/css/`, with
  interactivity from `static/js/`.
- **Application / Processing Layer** — the backend's future service
  modules (Import, Cleaning, Customization, Extraction, Statistical
  Analysis, Visualization, Conversion, Word Report Generator [deferred],
  Mock Data Generation, Automation, API Integration, Export), organized
  under `app/services/`. **Empty in Phase 00** except for the shared
  contracts in `app/processing/contracts.py`.
- **Data Abstraction Layer** — in-memory dataset/session state (pandas
  DataFrames per the SRS; no database). Phase 00 defines the
  `DatasetState` contract shape only; no real DataFrame storage exists yet.
- **Integration Layer** — the future API Integration module (FR-11).
  Not implemented in Phase 00.

## FR numbering — corrected and now canonical

The SRS and the Master UI Guidelines' own SRS-traceability matrix agree
with each other on FR numbers; the Master Context roadmap table disagreed
with both. Per the project owner's instruction, **this project now uses
the SRS numbering as canonical**:

| FR | Module |
|---|---|
| FR-01 | Data Import |
| FR-02 | Data Cleaning |
| FR-03 | Data Customization |
| FR-04 | Data Extraction |
| FR-05 | Data Visualization |
| FR-06 | Statistical Analysis |
| FR-07 | File Conversion |
| FR-08 | Word Report Generator (deferred until Phase 12) |
| FR-09 | Mock Data Generation |
| FR-10 | Automation |
| FR-11 | API Integration |
| FR-12 | Data Export |

If the Master Context document is revised, its roadmap table's FR column
should be updated to match this table rather than the reverse.

## One working dataset

Statistical Analysis and Visualization must never mutate the working
dataset. View-only Data Preview operations (search/filter/sort/column
visibility/order) are presentation state, not dataset mutation. The
`DatasetState` contract and the "view vs. dataset" distinction are modeled
in `app/processing/contracts.py` and will be enforced by the services that
implement it in later phases.

## Shared state contracts (Phase 00)

- `DatasetState` — dataset identity, lineage (`original_dataset_id`),
  modification flag, row/column counts.
- `DataFrameProcessingService` — abstract interface (`get_state` /
  `apply_operation`) that later phases implement per-module.
- JSON response envelope — `success_envelope()` / error envelope in
  `app/core/errors.py` — every future JSON endpoint should use this shape.

## Theming architecture

Four themes (Arctic Blue, Warm Pearl, Midnight Blue, Graphite) are
implemented as plain CSS custom-property sets keyed by a `data-theme`
attribute on `<html>` (`static/css/themes/*.css`), layered over shared
structural tokens (spacing, radius, typography, motion) in
`static/css/tokens.css`. An inline script in `templates/base.html` applies
the stored theme before first paint to avoid a flash of the wrong theme;
`static/js/theme.js` handles switching afterward and persists the choice
in `localStorage`. This lets later phases build templates/macros against
semantic variable names (`--pp-color-surface-1`, `--pp-color-text-primary`,
etc.) without knowing which theme is active.

## Reusable UI primitives

Implemented as Jinja macros in `templates/macros/ui.html` (Button, Input,
Select, Card, Status, Loading, Empty/Error state, Tooltip), matched by CSS
in `static/css/components/`. Any template can `{% import "macros/ui.html"
as ui %}` and use these consistently, mirroring the primitive set required
by the Master UI Guidelines without introducing a JS component framework.
