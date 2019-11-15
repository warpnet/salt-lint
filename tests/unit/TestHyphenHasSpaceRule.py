# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.HyphenHasSpaceRule import HyphenHasSpaceRule
from tests import RunFromText


GOOD_ONLY_ONE_SPACE = '''
/path/to/file1:
  file.managed:
    - contents: This is line 1
'''

BAD_TOO_MANY_SPACES = '''
/path/to/file2:
  file.managed:
    -  contents: This is line 2
'''

BAD_NO_SPACE = '''
/path/to/file3:
  file.managed:
    -contents: This is line 3
'''

class TestCommentFormatRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(HyphenHasSpaceRule())
        self.runner = RunFromText(self.collection)

    def test_only_one_space(self):
        results = self.runner.run_state(GOOD_ONLY_ONE_SPACE)
        self.assertEqual(0, len(results))

    def test_too_many_spaces(self):
        results = self.runner.run_state(BAD_TOO_MANY_SPACES)
        self.assertEqual(3, len(results))

    def test_no_space(self):
        results = self.runner.run_state(BAD_NO_SPACE)
        self.assertEqual(1, len(results))
