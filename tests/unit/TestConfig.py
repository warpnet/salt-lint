# -*- coding: utf-8 -*-
# Copyright (c) 2019 Roald Nefs

import unittest
import tempfile

from saltlint.config import SaltLintConfig


SALT_LINT_CONFIG = '''
---
exclude_paths:
  - exclude_this_file
  - exclude_this_directory/
  - exclude/this/sub-directory/
skip_list:
  - 207
  - 208
tags:
  - formatting
verbosity: 1
rules:
  formatting:
    ignore: |
      tests/test-extension-failure
      tests/**/*.jinja
'''

class TestConfig(unittest.TestCase):

    def setUp(self):
        # Open the temporary configuration file and write the contents of
        # SALT_LINT_CONFIG to the temporary file.
        fp = tempfile.NamedTemporaryFile()
        fp.write(SALT_LINT_CONFIG.encode())
        fp.seek(0)
        self.fp = fp

        # Specify the temporary file as if it wass passed as a command line
        # argument.
        self.config = SaltLintConfig(dict(c = self.fp.name))

    def tearDown(self):
        # Close the temporary configuration file.
        self.fp.close()

    def test_config(self):
        # Check 'verbosity'
        self.assertEqual(self.config.verbosity, 1)

        # Check 'skip_list'
        self.assertIn('208', self.config.skip_list)
        self.assertNotIn('200', self.config.skip_list)

        # Check 'exclude_paths'
        self.assertIn('exclude_this_file', self.config.exclude_paths)
        self.assertEqual(3, len(self.config.exclude_paths))

    def test_is_file_ignored(self):
        # Check basic ignored rules per file
        self.assertTrue(
            self.config.is_file_ignored('tests/test-extension-failure', 'formatting')
        )
        self.assertFalse(
            self.config.is_file_ignored('tests/test-extension-failure', '210')
        )
        # Check more complex ignored rules per file using gitwildmatches
        self.assertTrue(
            self.config.is_file_ignored('tests/other/test.jinja', 'formatting')
        )
        self.assertFalse(
            self.config.is_file_ignored('test.jinja', 'formatting')
        )


