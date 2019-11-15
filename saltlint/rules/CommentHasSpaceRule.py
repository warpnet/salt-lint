# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

from saltlint.linter import SaltLintRule
import re


class CommentHasSpaceRule(SaltLintRule):
    id = '213'
    shortdesc = 'Comment character should be always followed by at least one space.'
    description = 'Comment character should be always followed by at least one space.'
    severity = 'LOW'
    tags = ['formatting']
    version_added = 'v0.1.1'

    comment_regex = re.compile(r"(#[\w])")

    def match(self, file, line):
        return self.comment_regex.search(line)
