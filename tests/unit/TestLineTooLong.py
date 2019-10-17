# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.LineTooLongRule import LineTooLongRule
from tests import RunFromText

LONG_LINE = '''
/tmp/testfile:
  file.managed:
    - source:/salt://lorem/ipsum/dolor/sit/amet/consectetur/adipiscing/elit/sed/do/eiusmod/tempor/incididunt/ut/labore/et/dolore/magna/aliqua/ut/enim/ad/minim/veniam
'''


class TestLineTooLongRule(unittest.TestCase):
    collection = RulesCollection()
    collection.register(LineTooLongRule())

    def setUp(self):
        self.runner = RunFromText(self.collection)

    def test_long_line(self):
        results = self.runner.run_state(LONG_LINE)
        self.assertEqual(1, len(results))
