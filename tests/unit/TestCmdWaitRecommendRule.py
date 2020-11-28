# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.CmdWaitRecommendRule import CmdWaitRecommendRule
from tests import RunFromText


GOOD_CMD_STATE = '''
run_postinstall:
  cmd.run:
    - name: echo hello
    - cwd: /
    - onchanges:
        - pkg: mycustompkg
'''

BAD_CMD_STATE = '''
run_postinstall:
  cmd.wait:
    - name: /usr/local/bin/postinstall.sh
    - watch:
      - pkg: mycustompkg
'''

class TestCmdWaitRecommendRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(CmdWaitRecommendRule())

    def test_statement_positive(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(GOOD_CMD_STATE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(BAD_CMD_STATE)
        self.assertEqual(1, len(results))
