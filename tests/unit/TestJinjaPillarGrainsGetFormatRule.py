# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Jeffrey Bouter

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.JinjaPillarGrainsGetFormatRule import JinjaPillarGrainsGetFormatRule
from tests import RunFromText


GOOD_STATEMENT_LINE = '''
example_test:
  file.managed:
    - name: /etc/test
    - user: root
    - group: {{ salt['pillar.get']('item') }} test
    - something: {{ grains['item'] }}
    - content: |
        {{ salt['pillar.get']('test') }}
'''

BAD_STATEMENT_LINE = '''
example_test:
  file.managed:
    - name: /etc/test
    - user: root
    - group: {{ pillar.get('item') }} test
    - something: {{ grains.get('item')}}
    - content: |
        {{ salt['pillar.get']('test') }}
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
