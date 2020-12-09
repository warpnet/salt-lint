# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import Rule
from saltlint.utils import LANGUAGE_JINJA, LANGUAGE_SLS


class JinjaVariableHasSpacesRule(Rule):
    id = '206'
    shortdesc = "Jinja variables should have spaces before and after: '{{ var_name }}'"
    description = "Jinja variables should have spaces before and after: '{{ var_name }}'"
    severity = 'LOW'
    languages = [LANGUAGE_SLS, LANGUAGE_JINJA]
    tags = ['formatting', 'jinja']
    version_added = 'v0.0.1'

    bracket_regex = re.compile(r"{{[^ \-\+\d]|{{[-\+][^ ]|[^ \-\+\d]}}|[^ {][-\+\d]}}")

    def match(self, file, line):
        return self.bracket_regex.search(line)
