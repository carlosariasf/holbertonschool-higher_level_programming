#!/usr/bin/python3
"""more comments"""


import unittest
from models.base import Base
import pep8


class TestCodeFormat(unittest.TestCase):
    """more comments"""

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            'models/base.py', 'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
