# -*- coding: utf-8 -*-
# Added bij Chris van Breeden, Copyright (c) 2020
#

import unittest

from saltlint.config import SaltLintConfig
from saltlint.linter import Runner, RulesCollection
from saltlint.rules.JinjaTemplateHasRightExtensionRule import JinjaTemplateHasRightExtensionRule

class TestJinjaTemplateHasRightExtensionRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(JinjaTemplateHasRightExtensionRule())

    def test_file_extension_positive(self):
        path = 'tests/test-jinja-template.right.j2'
        runner = Runner(self.collection, path, SaltLintConfig())
        self.assertEqual([], runner.run())

    def test_file_extenion_negative(self):
        path = 'tests/test-jinja-template.bad'
        runner = Runner(self.collection, path, SaltLintConfig())
        errors = runner.run()
        self.assertEqual(1, len(errors))
