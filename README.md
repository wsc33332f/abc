# abc

A small Python library for basic arithmetic helpers and host command execution.

## Installation

```bash
python -m pip install -e .
```

## Usage

```python
from abc_library import add, exec, subtract

print(add(2, 3))       # 5
print(subtract(5, 2))  # 3
print(exec("whoami"))  # current host user
```

`exec` runs the specified executable and arguments on the host without a shell.
Use it only with trusted commands. It returns standard output and raises an
exception if the executable cannot be started or exits unsuccessfully.

## Validation

```bash
python -m pytest -q
```
