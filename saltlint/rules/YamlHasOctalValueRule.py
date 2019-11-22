# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2019 Warpnet B.V.

from saltlint.linter import SaltLintRule
import re


class YamlHasOctalValueRule(SaltLintRule):
    id = '210'
    shortdesc = 'Numbers that start with `0` should always be encapsulated in quotation marks'
    description = 'Numbers that start with `0` should always be encapsulated in quotation marks'
    severity = 'HIGH'
    tags = ['formatting']
    version_added = 'v0.0.6'

    bracket_regex = re.compile(r"(?<=:)\s{0,}0[0-9]{1,}\s{0,}((?={#)|(?=#)|(?=$))")

    def match(self, file, line):
        return self.bracket_regex.search(line)
