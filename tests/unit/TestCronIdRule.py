# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.CronIdRule import CronIdRule
from tests import RunFromText


GOOD_CMD_STATE = '''
run_postinstall:
  cron.present:
    - name: echo hello
    - identifier: yes

run_postinstall2:
  cron.present:
  - name: echo hello
  - identifier: yes2

run_do_something:
  cron.present:
  - name: echo hello
  - identifier: yes2
  cmd.run:
  - name: echo hello

'''

BAD_CMD_STATE = '''
run_postinstall:
  cron.present:
    - name: echo hello

run_postinstall2:
  cron.present:
  - name: echo hello

run_do_something:
  cron.present:
  - name: echo hello
  cmd.run:
  - name: echo hello

run_do_something:
  cron.present:
  - name: echo hello
  # - identifier: bleh

'''

class TestCmdWaitRecommendRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(CronIdRule())

    def test_statement_positive(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(GOOD_CMD_STATE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(BAD_CMD_STATE)
        self.assertEqual(4, len(results))
