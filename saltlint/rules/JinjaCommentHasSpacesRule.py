# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2019 Warpnet B.V.

from saltlint.linter import SaltLintRule
import re


class JinjaCommentHasSpacesRule(SaltLintRule):
    id = '209'
    shortdesc = 'Jinja comment should have spaces before and after: {# comment #}'
    description = 'Jinja comment should have spaces before and after: ``{# comment #}``'
    severity = 'LOW'
    tags = ['formatting', 'jinja']
    version_added = 'v0.0.5'

    bracket_regex = re.compile(r"{#[^ \-\+]|{#[\-\+][^ ]|[^ \-\+]#}|[^ ][\-\+]#}")

    def match(self, file, line):
        return self.bracket_regex.search(line)
