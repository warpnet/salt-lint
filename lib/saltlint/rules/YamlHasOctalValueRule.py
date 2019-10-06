# Copyright (c) 2016, Will Thames and contributors
# Copyright (c) 2018, Ansible Project
# Modified work Copyright (c) 2019 Roald Nefs

from saltlint import SaltLintRule
import re


class YamlHasOctalValueRule(SaltLintRule):
    id = '210'
    shortdesc = 'Numbers that start with `0` should always be encapsulated in quotation marks'
    description = 'Numbers that start with `0` should always be encapsulated in quotation marks'
    severity = 'HIGH'
    tags = ['formatting']
    version_added = 'develop'

    bracket_regex = re.compile(r"(?<!['\"])0+[1-9]\d*(?!['\"])")

    def match(self, file, line):
        return self.bracket_regex.search(line)
