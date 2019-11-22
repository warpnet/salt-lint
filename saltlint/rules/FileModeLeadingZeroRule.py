# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2019 Warpnet B.V.

from saltlint.linter import SaltLintRule
import re


class FileModeLeadingZeroRule(SaltLintRule):
    id = '208'
    shortdesc = 'File modes should always contain a leading zero'
    description = 'File modes should always contain a leading zero'
    severity = 'LOW'
    tags = ['formatting']
    version_added = 'v0.0.3'

    bracket_regex = re.compile(r"^\s+- ((dir_)|(file_))?mode: ((')|(\"))?[0-9]{3}([\D]|$)")

    def match(self, file, line):
        return self.bracket_regex.search(line)
