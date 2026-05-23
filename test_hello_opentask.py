import subprocess
import sys
import unittest


class HelloOpenTaskTest(unittest.TestCase):
    def test_prints_expected_message(self):
        result = subprocess.run(
            [sys.executable, "hello_opentask.py"],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.stdout, "Hello OpenTask\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
