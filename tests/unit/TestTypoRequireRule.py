# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2020 Warpnet B.V.
# Copyright (c) 2021 Yury Bushmelev

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.TypoRequireRule import TypoRequireRule
from tests import RunFromText


GOOD_REQUIRE_LINE = '''
testfile:
  file.managed:
    - name: /tmp/testfile
    - user: root
    - group: root
    - mode: '0700'
    - require:
        - otherfile
    - require_in:
        - anotherfile
    - require_any:
        - yetanotherfile
        - onemorefile
'''

BAD_REQUIRE_LINE = '''
testfile:
  file.managed:
    - name: /tmp/badfile
    - user: root
    - group: root
    - mode: 0700
    - requires:
        - otherfile
    - requires_in:
        - anotherfile
    - requires_any:
        - yetanotherfile
        - onemorefile
'''

class TestTypoRequireRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(TypoRequireRule())
        self.runner = RunFromText(self.collection)

    def test_statement_positive(self):
        results = self.runner.run_state(GOOD_REQUIRE_LINE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        results = self.runner.run_state(BAD_REQUIRE_LINE)
        self.assertEqual(3, len(results))
