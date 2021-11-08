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

NETWORK_MANAGED_MODE = '''
bond0:
  network.managed:
    - type: bond
    - mode: 802.3ad
    - proto: static
    - ipaddr: 10.1.1.77
    - netmask: 255.255.255.0
    - gateway: 10.1.1.1
    - dns: 10.1.1.1
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

    def test_network_mode(self):
        """
        Ensure the mode argument in the network.managed state gets ignored. See
        related GitHub issue:
        https://github.com/warpnet/salt-lint/issues/255
        """
        results = self.runner.run_state(NETWORK_MANAGED_MODE)
        self.assertEqual(0, len(results))
