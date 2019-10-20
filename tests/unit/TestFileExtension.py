# -*- coding: utf-8 -*-
# Copyright (c) 2019 Roald Nefs

import unittest

from saltlint.config import SaltLintConfig
from saltlint.linter import Runner, RulesCollection
from saltlint.rules.FileExtensionRule import FileExtensionRule


class TestLineTooLongRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(FileExtensionRule())

    def test_file_positive(self):
        path = 'tests/test-extension-success.sls'
        runner = Runner(self.collection, path, SaltLintConfig())
        self.assertEqual([], runner.run())

    def test_file_negative(self):
        path = 'tests/test-extension-failure'
        runner = Runner(self.collection, path, SaltLintConfig())
        errors = runner.run()
        self.assertEqual(1, len(errors))
