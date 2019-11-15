# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.ColonFormatRule import ColonFormatRule
from tests import RunFromText


BAD_EXTRA_SPACE = '''
# the following code snippet would fail:
/path/to/file1:
  file.managed:
    - contents : This is line 1
'''

BAD_NO_SPACE_BRACKET = '''
# the following code snippet would fail:
/path/to/file1:
    file.managed:
      - contents:[]
'''

BAD_NO_SPACE_CURLY_BRACKET = '''
# the following code snippet would fail:
/path/to/file1:
    file.managed:
      - contents:{}
'''

GOOD_SPACE_BRACKET = '''
# the following code snippet would fail:
/path/to/file1:
    file.managed:
      - contents: []
'''

GOOD_SPACE_CURLY_BRACKET = '''
# the following code snippet would fail:
/path/to/file1:
    file.managed:
      - contents: {}
'''

GOOD_NO_EXTRA_SPACE = '''
# the following code snippet would pass:
/path/to/file1:
  file.managed:
    - contents: This is line 1
'''

GOOD_CORNER_CASE = '''
# the following code snippet would pass:
example_file:
  file.managed:
    - name: /etc/example.txt
    - contents: |
        line:with:colons:without:spaces
'''


class TestColonFormatRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(ColonFormatRule())
        self.runner = RunFromText(self.collection)

    def test_bad_extra_space(self):
        results = self.runner.run_state(BAD_EXTRA_SPACE)
        self.assertEqual(1, len(results))

    def test_bad_no_space_bracket(self):
        results = self.runner.run_state(BAD_NO_SPACE_BRACKET)
        self.assertEqual(2, len(results))

    def test_bad_no_space_curly_bracket(self):
        results = self.runner.run_state(BAD_NO_SPACE_CURLY_BRACKET)
        self.assertEqual(3, len(results))

    def test_good_space_bracket(self):
        results = self.runner.run_state(GOOD_SPACE_BRACKET)
        self.assertEqual(0, len(results))

    def test_good_space_curly_bracket(self):
        results = self.runner.run_state(GOOD_SPACE_CURLY_BRACKET)
        self.assertEqual(0, len(results))

    def test_good_no_extra_space(self):
        results = self.runner.run_state(GOOD_NO_EXTRA_SPACE)
        self.assertEqual(0, len(results))

    def test_good_corner_case(self):
        results = self.runner.run_state(GOOD_CORNER_CASE)
        self.assertEqual(0, len(results))
