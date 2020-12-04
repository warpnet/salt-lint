# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import Rule
from saltlint.utils import LANGUAGE_SLS


class FileModeLeadingZeroRule(Rule):
    id = '208'
    shortdesc = 'File modes should always contain a leading zero'
    description = 'File modes should always contain a leading zero'
    severity = 'LOW'
    languages = [LANGUAGE_SLS]
    tags = ['formatting']
    version_added = 'v0.0.3'

    regex = re.compile(r"^\s+- ((dir_)|(file_))?mode: ((')|(\"))?[0-9]{3}([\D]|$)")

    def match(self, file, line):
        return self.regex.search(line)
