# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

from saltlint.linter import SaltLintRule
import re


class ColonFormatRule(SaltLintRule):
    id = '214'
    shortdesc = 'The line should have an proper colons formatting.'
    description = 'The line should have an proper colons formatting.'
    severity = 'MEDIUM'
    tags = ['formatting']
    version_added = 'v0.1.1'

    regex = re.compile(r"([\s]{1,}:)|((:\{)(?!\{))|(:\[)")

    def match(self, file, line):
        return self.regex.search(line)
