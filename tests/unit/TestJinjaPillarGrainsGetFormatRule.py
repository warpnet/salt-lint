# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.JinjaPillarGrainsGetFormatRule import JinjaPillarGrainsGetFormatRule
from tests import RunFromText


GOOD_STATEMENT_LINE = '''
example_file:
  file.managed:
    - name: /tmp/good.txt
    - contents: |
        {{ salt['pillar.get']('item') }}
        {{ pillar.get('item') }}
        {{ pillar['item'] }}
        {{ salt['grains.get']('saltversion') }}
        {{ grains.get('saltversion') }}
        {{ grains['saltversion'] }}
'''

BAD_STATEMENT_LINE = '''
example_file:
  file.managed:
    - name: /tmp/bad.txt
    - contents: |
        {{ salt['pillar.get']('item') }}
        {{ pillar.get('item') }}
        {{ pillar['item'] }}
        {{ pillar.get['item'] }} # this line is broken
        {{ salt['grains.get']('saltversion') }}
        {{ grains.get('saltversion') }}
        {{ grains['saltversion'] }}
        {{ grains.get['saltversion'] }} # this line is broken
'''

class TestJinjaPillarGrainsGetFormatRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(JinjaPillarGrainsGetFormatRule())
        self.runner = RunFromText(self.collection)

    def test_statement_positive(self):
        results = self.runner.run_state(GOOD_STATEMENT_LINE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        results = self.runner.run_state(BAD_STATEMENT_LINE)
        self.assertEqual(2, len(results))
