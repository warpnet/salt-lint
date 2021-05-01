# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2020 Warpnet B.V.
# Copyright (c) 2021 Yury Bushmelev

import re
from saltlint.linter.rule import Rule
from saltlint.utils import LANGUAGE_SLS


class TypoOnchangesRule(Rule):
    id = '216'
    shortdesc = '"onchange" looks like a typo. Did you mean "onchanges"?'
    description = '"onchange" looks like a typo. Did you mean "onchanges"?'
    severity = 'HIGH'
    languages = [LANGUAGE_SLS]
    tags = ['formatting']
    version_added = 'v0.5.3'

    regex = re.compile(r"^\s+- onchange(|_in|_any):")

    def match(self, file, line):
        return self.regex.search(line)
