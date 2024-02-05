# -*- coding: utf-8 -*-
# Copyright (c) 2024 Anton Ovseenko

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.EOFRule import EOFRule
from tests import RunFromText

NO_NEWLINE = '''
debug_output:
  cmd.run:
    - name: echo hello'''

ONE_NEWLINE = '''
debug_output:
  cmd.run:
    - name: echo hello
'''

TWO_NEWLINE = '''
debug_output:
  cmd.run:
    - name: echo hello

'''


class TestEOFRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(EOFRule())
        self.runner = RunFromText(self.collection)

    def test_eof_positive(self):
        results = self.runner.run_state(ONE_NEWLINE)
        self.assertEqual(0, len(results))

    def test_eof_negative(self):
        results = self.runner.run_state(TWO_NEWLINE)
        self.assertEqual(1, len(results))

    def test_eof_no_newline_negative(self):
        results = self.runner.run_state(NO_NEWLINE)
        self.assertEqual(1, len(results))
