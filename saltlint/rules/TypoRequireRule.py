# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2020 Warpnet B.V.
# Copyright (c) 2021 Yury Bushmelev

import re
from saltlint.linter.rule import Rule
from saltlint.utils import LANGUAGE_SLS


class TypoRequireRule(Rule):
    id = '217'
    shortdesc = '"requires" looks like a typo. Did you mean "require"?'
    description = '"requires" looks like a typo. Did you mean "require"?'
    severity = 'HIGH'
    languages = [LANGUAGE_SLS]
    tags = ['formatting']
    version_added = 'v0.5.3'

    regex = re.compile(r"^\s+- requires(|_in|_any):")

    def match(self, file, line):
        return self.regex.search(line)
