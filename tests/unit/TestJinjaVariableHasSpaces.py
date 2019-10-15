# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

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

class TestLineTooLongRule(unittest.TestCase):
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
