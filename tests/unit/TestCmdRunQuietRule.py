# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.CmdRunQuietRule import CmdRunQuietRule
from tests import RunFromText


GOOD_QUIET_STATE = '''
getpip:
  cmd.run:
    - name: /usr/bin/python /usr/local/sbin/get-pip.py
    - unless: which pip
    - require:
      - pkg: python
      - file: /usr/local/sbin/get-pip.py
    - output_loglevel: quiet
'''

BAD_QUIET_STATE = '''
getpip:
  cmd.run:
    - name: /usr/bin/python /usr/local/sbin/get-pip.py
    - unless: which pip
    - require:
      - pkg: python
      - file: /usr/local/sbin/get-pip.py
    - quiet  # This is the ninth line

getpip2:
  cmd.run:
    - name: /usr/bin/python /usr/local/sbin/get-pip.py
    - quiet

getpip3:
  cmd.run:
    - name: /usr/bin/python /usr/local/sbin/get-pip.py
    - quiet # noqa: 901

# Allow quiet option to be encapsulated by Jinja statements
get_pip_jinja:
  cmd.run:
    - name: /usr/bin/python /usr/local/sbin/get-pip.py
{% if pillar.get('quiet') %}
    - quiet
{% endif %}
'''

class TestCmdRunQuietRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(CmdRunQuietRule())

    def test_statement_positive(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(GOOD_QUIET_STATE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(BAD_QUIET_STATE)
        self.assertEqual(3, len(results))

        # Check line numbers of the results
        self.assertEqual(9, results[0].linenumber)
        self.assertEqual(14, results[1].linenumber)
