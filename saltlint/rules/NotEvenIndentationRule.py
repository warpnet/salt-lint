# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

import re
from saltlint.linter import SaltLintRule


class NotEvenIndentationRule(SaltLintRule):
    id = '215'
    shortdesc = 'The line should have an even indentation.'
    description = 'The line should have an even indentation.'
    severity = 'MEDIUM'
    tags = ['formatting']
    version_added = 'develop'

    regex = re.compile(r"(^\s{1}[\w])|(^\s{3}[\w])|(^\s{5}[\w])|(^\s{7}[\w])|(^\s{9}[\w])")

    def match(self, _, line):
        return self.regex.search(line)
