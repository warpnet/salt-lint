# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.NoTabsRule import NoTabsRule
from tests import RunFromText

LINE_WITH_TABS = '''
/tmp/testfile:
	file.managed:
	- source:/salt://lorem/ipsum/dolor
'''

LINE_WITH_SPACES = '''
/tmp/testfile:
  file.managed:
    - source:/salt://lorem/ipsum/dolor
'''

LINE_MIXED_TAB_SPACE = '''
/tmp/testfile:
  file.managed:
	- source:/salt://lorem/ipsum/dolor
'''


class TestNoTabsRule(unittest.TestCase):
    collection = RulesCollection()
    collection.register(NoTabsRule())

    def setUp(self):
        self.runner = RunFromText(self.collection)

    def test_with_tabs(self):
        results = self.runner.run_state(LINE_WITH_TABS)
        self.assertEqual(2, len(results))

    def test_with_spaces(self):
        results = self.runner.run_state(LINE_WITH_SPACES)
        self.assertEqual(0, len(results))

    def test_mixed_tab_space(self):
        results = self.runner.run_state(LINE_MIXED_TAB_SPACE)
        self.assertEqual(1, len(results))
