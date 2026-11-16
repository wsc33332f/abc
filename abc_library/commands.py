"""Host command execution helpers."""

import shlex
import subprocess


def exec(command: str) -> str:
    """Run a command on the host without a shell and return its standard output.

    Raises ``ValueError`` for an empty command and propagates process errors,
    including ``FileNotFoundError`` and ``subprocess.CalledProcessError``.
    """
    arguments = shlex.split(command)
    if not arguments:
        raise ValueError("command must not be empty")

    result = subprocess.run(arguments, capture_output=True, text=True, check=True)
    return result.stdout


__all__ = ["exec"]
