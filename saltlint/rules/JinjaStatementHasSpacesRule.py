# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import Rule
from saltlint.utils import LANGUAGE_JINJA, LANGUAGE_SLS


class JinjaStatementHasSpacesRule(Rule):
    id = '202'
    shortdesc = "Jinja statement should have spaces before and after: '{% statement %}'"
    description = "Jinja statement should have spaces before and after: '{% statement %}'"
    severity = 'LOW'
    languages = [LANGUAGE_SLS, LANGUAGE_JINJA]
    tags = ['formatting', 'jinja']
    version_added = 'v0.0.2'

    bracket_regex = re.compile(r"{%[^ \-\+]|{%[\-\+][^ ]|[^ \-\+]%}|[^ ][\-\+]%}")

    def match(self, file, line):
        return self.bracket_regex.search(line)
