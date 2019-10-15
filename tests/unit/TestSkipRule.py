# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.LineTooLongRule import LineTooLongRule
from saltlint.rules.JinjaVariableHasSpacesRule import JinjaVariableHasSpacesRule
from tests import RunFromText

LINE = '''
/tmp/testfile:
  file.managed:
    - source: salt://lorem/ipsum/dolor/sit/amet/consectetur/adipiscing/elit/sed/do/eiusmod/tempor/incididunt/ut/labore/et/dolore/magna/aliqua/ut/enim/ad/minim/veniam
'''

LINE_SKIP = '''
/tmp/testfile:
  file.managed:
    - source: salt://lorem/ipsum/dolor/sit/amet/consectetur/adipiscing/elit/sed/do/eiusmod/tempor/incididunt/ut/labore/et/dolore/magna/aliqua/ut/enim/ad/minim/veniam  # noqa: 204
'''

LINE_SKIP_MULTIPLE = '''
/tmp/testfile:
  file.managed:
    - source: salt://{{ lorem}}/ipsum/dolor/sit/amet/consectetur/adipiscing/elit/sed/do/eiusmod/tempor/incididunt/ut/labore/et/dolore/magna/aliqua/ut/enim/ad/minim/veniam  # noqa: 204 206
'''


class TestSkipRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(LineTooLongRule())
        self.collection.register(JinjaVariableHasSpacesRule())

    def test_no_skip_rule(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(LINE)
        self.assertEqual(1, len(results))

    def test_skip_multiple_rules(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(LINE_SKIP_MULTIPLE)
        self.assertEqual(0, len(results))

    def test_skip_rule(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(LINE_SKIP)
        self.assertEqual(0, len(results))


