# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.NoIrregularSpacesRule import NoIrregularSpacesRule
from tests import RunFromText


try:
    # Python 2: "unicode" is built-in
    unicode
except NameError:
    unicode = str


LINE = '''
/tmp/testfile:
    file.managed:
      - content:{space}"foobar"
'''


class TestNoIrregularSpacesRule(unittest.TestCase):
    collection = RulesCollection()
    collection.register(NoIrregularSpacesRule())

    def setUp(self):
        self.runner = RunFromText(self.collection)

    def test_with_irregular_spaces(self):
        for irregular in NoIrregularSpacesRule.irregular_spaces:
            results = self.runner.run_state(unicode(LINE).format(space=irregular))
            self.assertEqual(1, len(results))

    def test_without_irregular_spaces(self):
        results = self.runner.run_state(LINE.format(space=" "))
        self.assertEqual(0, len(results))
