# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.NestedDictRule import NestedDictRule
from tests import RunFromText


GOOD_NESTED_DICT_STATE = """
/etc/http/conf/http.conf:
  file.managed:
    - source: salt://apache/http.conf
    - template: jinja
    - context:
        custom_var: "override"
    - defaults:
        custom_var: "default value"
        other_var: 123

/etc/http/conf/http.conf:
  file.managed:
    - source: salt://apache/http.conf
    - mode: 644
    - template: jinja
    - context: { custom_var: "override" }
    - defaults: {
      custom_var: "default value",
      other_var: 123
      }


/etc/http/conf/http.conf:
    file.managed:
        - source: salt://apache/http.conf
        - template: jinja
        - context:
              custom_var: "override"
        - defaults:
            custom_var: "default value"
            other_var: 123

/etc/http/conf/http.conf:
  file.managed:
    - source: salt://apache/http.conf
    - template: jinja
    - context:
      custom_var: "override"  # noqa: 219
    - defaults:
        custom_var: "default value"
        other_var: 123

/etc/http/conf/http.conf:
  file.managed:
    - source: salt://apache/http.conf
    - template: jinja
    - context:  # noqa: 219
      custom_var: "override"
    - defaults:
        custom_var: "default value"
        other_var: 123
"""

BAD_NESTED_DICT_STATE = """
/etc/http/conf/http.conf:
  file.managed:
    - source: salt://apache/http.conf
    - template: jinja
    - context:
      custom_var: "override"
    - defaults:
        custom_var: "default value"
        other_var: 123

/etc/http/conf/http.conf:
  file.managed:
    - source: salt://apache/http.conf
    - template: jinja
    - context:
        custom_var: "override"
    - defaults:
      custom_var: "default value"
      other_var: 123

/etc/http/conf/http.conf:
  file.managed:
    - source: salt://apache/http.conf
    - template: jinja
    - context:
      custom_var: "override"
    - defaults:
      custom_var: "default value"
      other_var: 123
"""


class TestNestedDictRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(NestedDictRule())

    def test_statement_positive(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(GOOD_NESTED_DICT_STATE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(BAD_NESTED_DICT_STATE)
        self.assertEqual(4, len(results))

        # Check line numbers of the results
        self.assertEqual(7, results[0].linenumber)
        self.assertEqual(19, results[1].linenumber)
        self.assertEqual(27, results[2].linenumber)
        self.assertEqual(29, results[3].linenumber)
