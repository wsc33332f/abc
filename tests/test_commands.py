import shlex
import subprocess
import sys
import unittest

from abc_library import exec


class TestCommandExecution(unittest.TestCase):
    def test_exec_returns_standard_output(self):
        command = f"{shlex.quote(sys.executable)} -c \"print('command output')\""

        self.assertEqual(exec(command), "command output\n")

    def test_exec_rejects_empty_command(self):
        with self.assertRaises(ValueError):
            exec(" ")

    def test_exec_raises_for_nonzero_exit(self):
        command = f"{shlex.quote(sys.executable)} -c \"raise SystemExit(1)\""

        with self.assertRaises(subprocess.CalledProcessError):
            exec(command)


if __name__ == "__main__":
    unittest.main()
