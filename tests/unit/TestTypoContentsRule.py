# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2020 Warpnet B.V.
# Copyright (c) 2021 Yury Bushmelev

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.TypoContentsRule import TypoContentsRule
from tests import RunFromText


GOOD_CONTENTS_LINE = '''
testfile:
  file.managed:
    - name: /tmp/testfile
    - user: root
    - group: root
    - mode: '0700'
    - contents: test
    - contents_pillar: foo
    - contents_grains: bar
    - contents_newline: True
    - contents_delimiter: '!'
'''

BAD_CONTENTS_LINE = '''
testfile:
  file.managed:
    - name: /tmp/badfile
    - user: root
    - group: root
    - mode: 0700
    - content: test
    - content_pillar: foo
    - content_grains: bar
    - content_newline: True
    - content_delimiter: '!'
'''

class TestTypoContentsRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(TypoContentsRule())
        self.runner = RunFromText(self.collection)

    def test_statement_positive(self):
        results = self.runner.run_state(GOOD_CONTENTS_LINE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        results = self.runner.run_state(BAD_CONTENTS_LINE)
        self.assertEqual(5, len(results))
