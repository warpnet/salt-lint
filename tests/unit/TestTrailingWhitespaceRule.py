# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.TrailingWhitespaceRule import TrailingWhitespaceRule
from tests import RunFromText

LINE_AND_WHITESPACE = '''
/tmp/testfile:
  file.managed:
    - source:/salt://lorem/ipsum/dolor  '''


class TestTrailingWhitespaceRule(unittest.TestCase):
    collection = RulesCollection()
    collection.register(TrailingWhitespaceRule())

    def setUp(self):
        self.runner = RunFromText(self.collection)

    def test_trailing_whitespace(self):
        results = self.runner.run_state(LINE_AND_WHITESPACE)
        print(results)
        self.assertEqual(1, len(results))
