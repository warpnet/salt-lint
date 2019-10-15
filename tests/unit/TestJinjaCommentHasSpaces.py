# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.JinjaCommentHasSpacesRule import JinjaCommentHasSpacesRule
from tests import RunFromText


GOOD_COMMENT_LINE = '''
{#- set example='good' +#}
'''

BAD_COMMENT_LINE = '''
{#-set example='bad'+#}
'''

class TestLineTooLongRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(JinjaCommentHasSpacesRule())
        self.runner = RunFromText(self.collection)

    def test_comment_positive(self):
        results = self.runner.run_state(GOOD_COMMENT_LINE)
        self.assertEqual(0, len(results))

    def test_comment_negative(self):
        results = self.runner.run_state(BAD_COMMENT_LINE)
        self.assertEqual(1, len(results))
