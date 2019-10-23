# -*- coding: utf-8 -*-
# Copyright (c) 2019 Roald Nefs

import unittest

from saltlint.cli import run

class TestRunner(unittest.TestCase):

    def test_runner_with_matches(self):
        # Check the integer returned by saltlint.cli.run(), when matches are
        # expected.
        args = ['tests/test-extension-failure']
        self.assertEqual(run(args), 2)

    def test_runner_without_matches(self):
        # Check the integer returned by saltlint.cli.run(), when no matches are
        # expected.
        args = ['tests/test-extension-success.sls']
        self.assertEqual(run(args), 0)