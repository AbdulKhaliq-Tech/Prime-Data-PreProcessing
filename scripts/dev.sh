#!/usr/bin/env bash
# Convenience script: load .env (if present) and start the dev server.
#
# Usage:
#   ./scripts/dev.sh
#
# Prerequisite: dependencies installed (pip install -r requirements.txt)
# and a .env file created (cp .env.example .env).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

if [ ! -f .env ]; then
  echo "No .env file found. Copying .env.example -> .env"
  cp .env.example .env
fi

python3 run.py
