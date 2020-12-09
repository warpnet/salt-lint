# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.StateDeprecationDockerAbsent import StateDeprecationDockerAbsent
from tests import RunFromText


GOOD_STATES_LINE = '''
example:
  docker_container.absent:
    - name: example

example:
  docker_container.absent
'''

BAD_STATES_LINE = '''
example:
  docker.absent:
    - name: example

example:
  docker.absent
'''

class TestFileModeLeadingZeroRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(StateDeprecationDockerAbsent())

    def test_statement_positive(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(GOOD_STATES_LINE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(BAD_STATES_LINE)
        self.assertEqual(2, len(results))
