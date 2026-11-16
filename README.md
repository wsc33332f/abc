# abc

A minimal Python library scaffold for experimentation and extension.

## Project layout
- `src/abc_lib/` contains the library package.
- `tests/` contains behavior tests.
- `.github/copilot-instructions.md` contains repository-specific agent guidance.

## Quick start

```bash
python -m pip install -e .
python -c "from abc_lib import format_message; print(format_message('Ada'))"
```

## Validation

```bash
python -m pytest -q
```
