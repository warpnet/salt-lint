# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.NewLineAtTheEndRule import NewLineAtTheEndRule
from tests import RunFromText


BAD_LAST_LINE = '''
/path/to/file1:
  file.managed:
    - contents: This is line 1
'''

GOOD_LAST_LINE = '''
/path/to/file1:
  file.managed:
    - contents: This is line 1

'''


class TestNewLineAtTheEndRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(NewLineAtTheEndRule())
        self.runner = RunFromText(self.collection)

    def test_bad_last_line(self):
        results = self.runner.run_state(BAD_LAST_LINE)
        self.assertEqual(1, len(results))

    def test_good_last_line(self):
        results = self.runner.run_state(GOOD_LAST_LINE)
        self.assertEqual(0, len(results))
