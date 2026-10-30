#!/usr/bin/env python3
"""The outer heredoc can parse even when the generated startup script cannot."""
from pathlib import Path
import re
import subprocess
import unittest


class StartedScriptTests(unittest.TestCase):
    def test_generated_default_script_parses(self):
        path = Path(__file__).resolve().parents[1] / "trunk/user/scripts/mtd_storage.sh"
        source = path.read_text()
        match = re.search(r'cat > "\$script_started" <<\x27EOF\x27\n(.*?)\nEOF', source, re.S)
        self.assertIsNotNone(match, "default startup script not found")
        result = subprocess.run(["sh", "-n"], input=match.group(1), text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
