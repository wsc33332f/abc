# Copilot instructions for this repository

## Repository context
- This repository is a Python library project, intentionally scaffolded as a small, maintainable package.
- The library code lives in `src/abc_lib/` and should stay organized in a `src` layout to keep packaging clear.
- Tests live under `tests/` and should validate public behavior rather than implementation details.

## Working conventions
- Prefer small, explicit modules and functions with type hints.
- Keep public APIs simple and documented with concise docstrings when useful.
- Write tests for user-visible behavior before or alongside new functionality.
- Avoid broad refactors or unrelated cleanup.
- Prefer standard-library features and lightweight dependencies unless the task clearly requires more.

## Validation
- Run the focused validation command for the repo after changes:
  - `python -m pytest -q`
- If a new dependency is needed, add it to `pyproject.toml` and keep the project minimal.

## Deliverables
- Preserve a clean package structure and keep the project easy for future contributors to extend.
- Update README documentation when behavior or setup changes.
