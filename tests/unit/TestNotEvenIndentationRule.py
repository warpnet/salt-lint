# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.NotEvenIndentationRule import NotEvenIndentationRule
from tests import RunFromText


GOOD_NUMBER_OF_SPACES = '''
# the following code snippet would pass:
/path/to/file1:
  file.managed:
    - contents: This is line 1
'''

BAD_ONE_SPACE = '''
# the following code snippet would fail:
/path/to/file1:
 file.managed:
    - contents: This is line 1
'''

BAD_FIVE_SPACES = '''
# the following code snippet would fail:
/path/to/file1:
     file.managed:
      - contents: This is line 1
'''


class TestNotEvenIndentationRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(NotEvenIndentationRule())
        self.runner = RunFromText(self.collection)

    def test_good_number_of_space(self):
        results = self.runner.run_state(GOOD_NUMBER_OF_SPACES)
        self.assertEqual(0, len(results))

    def test_bad_only_one_space(self):
        results = self.runner.run_state(BAD_ONE_SPACE)
        self.assertEqual(2, len(results))

    def test_bad_five_spaces(self):
        results = self.runner.run_state(BAD_FIVE_SPACES)
        self.assertEqual(1, len(results))
