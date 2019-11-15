# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.CommentHasSpaceRule import CommentHasSpaceRule
from tests import RunFromText


GOOD_ONLY_ONE_SPACE = '''
# This is file1
/path/to/file1:
  file.managed:
    - contents: This is line 1
'''

GOOD_MANY_SPACES = '''
#  This is file1
/path/to/file1:
  file.managed:
    - contents: This is line 1
'''

BAD_NO_SPACE = '''
#This is file1
/path/to/file1:
  file.managed:
    - contents: This is line 1
'''

BAD_COMMENT_BLOCK = '''
#Example pillar:
#
#item:
#  - list1
#  - list2
'''

GOOD_COMMENT_BLOCK = '''
# Example pillar:
#
# item:
#   - list1
#   - list2
'''

class TestCommentHasSpaceRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(CommentHasSpaceRule())
        self.runner = RunFromText(self.collection)

    def test_only_one_space(self):
        results = self.runner.run_state(GOOD_ONLY_ONE_SPACE)
        self.assertEqual(0, len(results))

    def test_many_spaces(self):
        results = self.runner.run_state(GOOD_MANY_SPACES)
        self.assertEqual(0, len(results))

    def test_no_space(self):
        results = self.runner.run_state(BAD_NO_SPACE)
        self.assertEqual(4, len(results))

    def test_bad_command_block(self):
        results = self.runner.run_state(BAD_COMMENT_BLOCK)
        self.assertEqual(2, len(results))

    def test_good_command_block(self):
        results = self.runner.run_state(GOOD_COMMENT_BLOCK)
        self.assertEqual(0, len(results))
