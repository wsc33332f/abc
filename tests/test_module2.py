import unittest

from abc_library import subtract


class TestMathFunctions(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)


if __name__ == "__main__":
    unittest.main()