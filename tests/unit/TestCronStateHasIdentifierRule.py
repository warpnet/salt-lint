# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.CronStateHasIdentifierRule import CronStateHasIdentifierRule
from tests import RunFromText


GOOD_CRON_STATE = '''
multi_state_test:
  cron.present:
    - name: "/myscript.sh"
    - identifier: MY_IDENTIFIER
    - hour: *
    - minute: "30"
    - require:
      - file: multi_state_test
  file.exists:
    - name: "/myscript.sh"

cron_with_identifier1:
  cron.present:
    - name: '/sbin/reboot'
    - user: root
    - minute: '00'
    - hour: *
    - identifier: hourly-reboot

cron_with_identifier2:
  cron.present:
    - name: '/sbin/reboot'
    - identifier: hourly-reboot
    - user: root
    - minute: '00'
    - hour: *
'''

BAD_CRON_STATE = '''
multi_state_test:
  cron.present:
    - name: "/myscript.sh"
    - hour: *
    - minute: "30"
  file.exists:
    - name: "/myscript.sh"

cron_without_identifier0:
  cron.present:
    - name: '/sbin/reboot'

cron_without_identifier1:
  cron.present:
    - name: '/sbin/reboot'
    - user: root
    - minute: '00'
    - hour: *

cron_without_identifier2:
  cron.present:
    - name: '/sbin/identifier'
    - user: root
    - minute: '00'
    - hour: *

cron_without_identifier3:
  cron.present:  # noqa: 801
    - name: '/sbin/identifier'
    - user: root
    - minute: '00'
    - hour: *
'''


class TestCronStateHasIdentifierRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(CronStateHasIdentifierRule())

    def test_statement_positive(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(GOOD_CRON_STATE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(BAD_CRON_STATE)
        self.assertEqual(4, len(results))

        # Check line numbers of the results
        self.assertEqual(3, results[0].linenumber)
        self.assertEqual(11, results[1].linenumber)
