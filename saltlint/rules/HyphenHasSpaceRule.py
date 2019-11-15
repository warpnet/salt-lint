# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

from saltlint.linter import SaltLintRule
import re


class HyphenHasSpaceRule(SaltLintRule):
    id = '216'
    shortdesc = 'Hyphen character should be always followed by the one space.'
    description = 'Hyphen character should be always followed by the one space.'
    severity = 'MEDIUM'
    tags = ['formatting']
    version_added = 'v0.1.1'

    comment_regex = re.compile(r"(-[\s]{2,}\w)|(\s{2,}-[\w])")

    def match(self, file, line):
        return self.comment_regex.search(line)
