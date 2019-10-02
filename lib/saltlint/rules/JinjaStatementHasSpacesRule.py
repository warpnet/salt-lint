# Copyright (c) 2016, Will Thames and contributors
# Copyright (c) 2018, Ansible Project
# Modified work Copyright (c) 2019 Roald Nefs

from saltlint import SaltLintRule
import re


class JinjaStatementHasSpacesRule(SaltLintRule):
    id = '202'
    shortdesc = 'Jinja statement should have spaces before and after: {% statement %}'
    description = 'Jinja statement should have spaces before and after: ``{% statement %}``'
    severity = 'LOW'
    tags = ['formatting']
    version_added = 'v0.0.1'

    bracket_regex = re.compile(r"{%[^ -]|{%-[^ ]|[^ -]%}|[^ ]-%}")

    def match(self, file, line):
        return self.bracket_regex.search(line)
