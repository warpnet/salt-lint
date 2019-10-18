# -*- coding: utf-8 -*-
# Copyright (c) 2019 Roald Nefs

import yaml
import os

# Import Salt libs
from salt.ext import six

from saltlint.linter import default_rulesdir


class SaltLintConfigError(Exception):
    pass


class SaltLintConfig(object):

    def __init__(self, options):
        self._options = options
        # Configuration file to use, defaults to ".salt-lint".
        file = options.c if options.c else '.salt-lint'

        # Read the file contents
        if os.path.exists(file):
            with open(file, 'r') as f:
                content = f.read()
        else:
            content = None

        # Parse the content of the file as YAML
        self._parse(content)
        self._validate()

    def _parse(self, content):
        config = dict()

        # Parse the YAML content
        if content:
            try:
                config = yaml.safe_load(content)
            except Exception as exc:
                raise SaltLintConfigError("invalid config: {}".format(exc))

        # Parse verbosity
        self.verbosity = self._options.verbosity
        if 'verbosity' in config:
            self.verbosity += config['verbosity']

        # Parse exclude paths
        self.exclude_paths = self._options.exclude_paths
        if 'exclude_paths' in config:
            self.exclude_paths += config['exclude_paths']

        # Parse skip list
        skip_list = self._options.skip_list
        if 'skip_list' in config:
            skip_list += config['skip_list']
        skip = set()
        for s in skip_list:
            skip.update(str(s).split(','))
        self.skip_list = frozenset(skip)

        # Parse tags
        self.tags = self._options.tags
        if 'tags' in config:
            self.tags += config['tags']
        if isinstance(self.tags, six.string_types):
            self.tags = self.tags.split(',')

        # Parse use default rules
        use_default_rules = self._options.use_default_rules
        if 'use_default_rules' in config:
            use_default_rules = use_default_rules or config['use_default_rules']

        # Parse rulesdir
        rulesdir = self._options.rulesdir
        if 'rulesdir' in config:
            rulesdir += config['rulesdir']

        # Determine the rules directories
        if use_default_rules:
            self.rulesdirs = rulesdir + [default_rulesdir]
        else:
            self.rulesdirs = rulesdir or [default_rulesdir]

        # Parse colored
        self.colored = self._options.colored

    def _validate(self):
        pass
