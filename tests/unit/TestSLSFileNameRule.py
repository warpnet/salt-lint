# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.config import Configuration
from saltlint.linter.runner import Runner
from saltlint.linter.collection import RulesCollection
from saltlint.rules.SLSFileNameRule import SLSFileNameRule


class TestSLSFileNameRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(SLSFileNameRule())

    def test_file_positive(self):
        path = 'tests/test-extension-success.sls'
        runner = Runner(self.collection, path, Configuration())
        self.assertEqual([], runner.run())

        path = 'tests/test-extension-failure'
        runner = Runner(self.collection, path, Configuration())
        self.assertEqual([], runner.run())

        path = 'tests/test-extension-failure.extra.jinja'
        runner = Runner(self.collection, path, Configuration())
        self.assertEqual([], runner.run())

    def test_file_negative(self):
        path = 'tests/test-extension-failure.extra.sls'
        runner = Runner(self.collection, path, Configuration())
        self.assertEqual(1, len(runner.run()))
