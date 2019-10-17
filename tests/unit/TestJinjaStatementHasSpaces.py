# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.JinjaStatementHasSpacesRule import JinjaStatementHasSpacesRule
from tests import RunFromText


GOOD_STATEMENT_LINE = '''
{%- set example='good' +%}
'''

BAD_STATEMENT_LINE = '''
{%-set example='bad'+%}
'''

class TestLineTooLongRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(JinjaStatementHasSpacesRule())
        self.runner = RunFromText(self.collection)

    def test_statement_positive(self):
        results = self.runner.run_state(GOOD_STATEMENT_LINE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        results = self.runner.run_state(BAD_STATEMENT_LINE)
        self.assertEqual(1, len(results))
