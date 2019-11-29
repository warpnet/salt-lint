# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

import unittest

from saltlint.linter import RulesCollection
from saltlint.rules.StateCanBeRendered import StateCanBeRendered
from tests import RunFromText


BAD_SLS_FILE = '''
# the following code snippet would fail:
/path/to/file1
  file.managed:
    - contents: This is line 1

'''

GOOD_SLS_FILE = '''
# the following code snippet would fail:
/path/to/file1:
    file.managed:
      - contents: This is line 1

'''


class TestStateCanBeRendered(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(StateCanBeRendered())
        self.runner = RunFromText(self.collection)

    def test_bad_sls_file(self):
        results = self.runner.run_state(BAD_SLS_FILE)
        self.assertEqual(1, len(results))

    def test_good_sls_file(self):
        results = self.runner.run_state(GOOD_SLS_FILE)
        self.assertEqual(0, len(results))
