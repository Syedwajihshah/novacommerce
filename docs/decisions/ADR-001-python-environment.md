# ADR-001: Python Environment Management

## Status
Accepted

## Context
Ubuntu 20.04 uses Python 3.8.10 as the system Python. NovaCommerce requires a modern Python runtime without modifying the operating system's Python installation.

## Decision
NovaCommerce will use Python 3.12 managed through `uv`.

Each project will use its own `.venv` virtual environment.

`uv` will manage:
- the project Python version
- virtual environment
- Python dependencies
- dependency locking through `uv.lock`

## Why
This keeps NovaCommerce isolated from Ubuntu's system Python and makes the project easier to reproduce on another machine.

## Consequences
- Ubuntu's system Python remains unchanged.
- NovaCommerce uses Python 3.12 independently.
- Developers should use `uv sync`, `uv add`, and `uv run` for project dependency and execution workflows.