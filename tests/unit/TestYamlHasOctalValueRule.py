# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.YamlHasOctalValueRule import YamlHasOctalValueRule
from tests import RunFromText


GOOD_NUMBER_LINE = '''
testdirectory:
  file.recurse:
    - name: /tmp/directory
    - file_mode: 700
    - dir_mode: '0775'

testdirectory02:
  file.recurse:
    - name: /tmp/directory02
    - file_mode: 0
    - dir_mode: "0775"
'''

BAD_NUMBER_LINE = '''
testdirectory:
  file.recurse:
    - name: /tmp/directory001  # shouldn't fail
    - mode: 0                  # shouldn't fail
    - file_mode: 00            # should fail
    - dir_mode: 0700           # should fail
'''

class TestFileModeLeadingZeroRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(YamlHasOctalValueRule())

    def test_statement_positive(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(GOOD_NUMBER_LINE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(BAD_NUMBER_LINE)
        self.assertEqual(2, len(results))
