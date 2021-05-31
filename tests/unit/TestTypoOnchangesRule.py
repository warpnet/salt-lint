# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2020 Warpnet B.V.
# Copyright (c) 2021 Yury Bushmelev

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.TypoOnchangesRule import TypoOnchangesRule
from tests import RunFromText


GOOD_ONCHANGES_LINE = '''
testfile:
  file.managed:
    - name: /tmp/testfile
    - user: root
    - group: root
    - mode: '0700'
    - onchanges:
        - otherfile
    - onchanges_in:
        - anotherfile
    - onchanges_any:
        - yetanotherfile
        - onemorefile
'''

BAD_ONCHANGES_LINE = '''
testfile:
  file.managed:
    - name: /tmp/badfile
    - user: root
    - group: root
    - mode: 0700
    - onchange:
        - otherfile
    - onchange_in:
        - anotherfile
    - onchange_any:
        - yetanotherfile
        - onemorefile
'''

class TestTypoOnchangesRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(TypoOnchangesRule())
        self.runner = RunFromText(self.collection)

    def test_statement_positive(self):
        results = self.runner.run_state(GOOD_ONCHANGES_LINE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        results = self.runner.run_state(BAD_ONCHANGES_LINE)
        self.assertEqual(3, len(results))
