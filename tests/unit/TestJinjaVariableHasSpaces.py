# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Warpnet B.V.

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.JinjaVariableHasSpacesRule import JinjaVariableHasSpacesRule
from tests import RunFromText


GOOD_VARIABLE_LINE = '''
{{- variable +}}
'''

BAD_VARIABLE_LINE = '''
{{-variable+}}
'''

BAD_VARIABLE_ENDING_IN_INTEGER = '''
{{-variable0+}}
'''

BAD_VARIABLE_ENDING_IN_INTEGER_RIGHT = '''
{{ variable0}}
'''

DOUBLE_QUOTED_INTEGER_IS_VALID = '''
{{ "{{0}}" }}
'''

DOUBLE_QUOTED_INTEGER_TRAILING_SPACE_IS_INVALID = '''
{{ "{{0}}"}}
'''

DOUBLE_QUOTED_INTEGER_LEADING_SPACE_IS_INVALID = '''
{{"{{0}}" }}
'''

class TestJinjaVariableHasSpaces(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(JinjaVariableHasSpacesRule())
        self.runner = RunFromText(self.collection)

    def test_statement_positive(self):
        results = self.runner.run_state(GOOD_VARIABLE_LINE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        results = self.runner.run_state(BAD_VARIABLE_LINE)
        self.assertEqual(1, len(results))

    def test_double_quoted_integer(self):
        results = self.runner.run_state(DOUBLE_QUOTED_INTEGER_IS_VALID)
        self.assertEqual(0, len(results))

    def test_double_quoted_integer_trailing_space_invalid(self):
        results = self.runner.run_state(DOUBLE_QUOTED_INTEGER_TRAILING_SPACE_IS_INVALID)
        self.assertEqual(1, len(results))

    def test_double_quoted_integer_leading_space_invalid(self):
        results = self.runner.run_state(DOUBLE_QUOTED_INTEGER_LEADING_SPACE_IS_INVALID)
        self.assertEqual(1, len(results))

    def test_variable_bad_ends_with_integer(self):
        results = self.runner.run_state(BAD_VARIABLE_ENDING_IN_INTEGER)
        self.assertEqual(1, len(results))

    def test_variable_bad_ends_with_integer_right(self):
        results = self.runner.run_state(BAD_VARIABLE_ENDING_IN_INTEGER_RIGHT)
        self.assertEqual(1, len(results))
