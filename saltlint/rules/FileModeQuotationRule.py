# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2019 Warpnet B.V.

import re
from saltlint.linter import SaltLintRule


class FileModeQuotationRule(SaltLintRule):
    id = '207'
    shortdesc = 'File modes should always be encapsulated in quotation marks'
    description = 'File modes should always be encapsulated in quotation marks'
    severity = 'HIGH'
    tags = ['formatting']
    version_added = 'v0.0.3'

    bracket_regex = re.compile(r"^\s+- ((dir_)|(file_))?mode: [0-9]{3,4}")

    def match(self, _, line):
        return self.bracket_regex.search(line)
