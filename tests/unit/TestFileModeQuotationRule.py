# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.FileModeQuotationRule import FileModeQuotationRule
from tests import RunFromText


GOOD_MODE_QUOTATION_LINE = '''
testfile:
  file.managed:
    - name: /tmp/testfile
    - user: root
    - group: root
    - mode: '0700'
'''

BAD_MODE_QUOTATION_LINE = '''
testfile:
  file.managed:
    - name: /tmp/badfile
    - user: root
    - group: root
    - mode: 0700
    - file_mode: 0660
    - dir_mode: 0775
'''

MODE_MISSING_QUOTATION_LINE = '''
testfile:
  file.managed:
    - name: /tmp/badfile
    - user: root
    - group: root
    - mode: "0700
    - file_mode: '0660
    - dir_mode: 0775"
'''


class TestModeQuotationRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(FileModeQuotationRule())
        self.runner = RunFromText(self.collection)

    def test_statement_positive(self):
        results = self.runner.run_state(GOOD_MODE_QUOTATION_LINE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        results = self.runner.run_state(BAD_MODE_QUOTATION_LINE)
        self.assertEqual(3, len(results))

    def test_missing_quotes(self):
        results = self.runner.run_state(MODE_MISSING_QUOTATION_LINE)
        self.assertEqual(3, len(results))
