# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

import re
from saltlint.linter import SaltLintRule


class CommentHasSpaceRule(SaltLintRule):
    id = '213'
    shortdesc = 'Comment character should be always followed by at least one space.'
    description = 'Comment character should be always followed by at least one space.'
    severity = 'LOW'
    tags = ['formatting']
    version_added = 'develop'

    comment_regex = re.compile(r"(#[\w])")

    def match(self, file, line):
        # pylint: disable=unused-argument
        return self.comment_regex.search(line)
