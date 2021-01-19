# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.cli import run
from saltlint.config import Configuration
from saltlint.linter.runner import Runner


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

    def test_runner_exclude_paths(self):
        """
        Check if all the excluded paths from the configuration are passed to
        the runner.
        """
        exclude_paths = ['first.sls', 'second.sls']
        config = Configuration(dict(exclude_paths=exclude_paths))
        runner = Runner([], 'init.sls', config)

        self.assertTrue(
            any(path in runner.exclude_paths for path in exclude_paths)
        )
