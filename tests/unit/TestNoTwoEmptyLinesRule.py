# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.NoTwoEmptyLinesRule import NoTwoEmptyLinesRule
from tests import RunFromText


BAD_LINES = '''
/path/to/file1:
  file.managed:
    - contents: This is line 1


/path/to/file2:
  file.managed:
    - contents: This is line 2
'''

GOOD_LINES = '''
/path/to/file1:
  file.managed:
    - contents: This is line 1

/path/to/file2:
  file.managed:
    - contents: This is line 2
'''


class TestNoTwoEmptyLinesRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(NoTwoEmptyLinesRule())
        self.runner = RunFromText(self.collection)

    def test_bad_lines(self):
        results = self.runner.run_state(BAD_LINES)
        self.assertEqual(1, len(results))

    def test_good_lines(self):
        results = self.runner.run_state(GOOD_LINES)
        self.assertEqual(0, len(results))
