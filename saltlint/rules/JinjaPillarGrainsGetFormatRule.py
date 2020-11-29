# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import Rule
from saltlint.utils import LANGUAGE_JINJA, LANGUAGE_SLS


class JinjaPillarGrainsGetFormatRule(Rule):
    id = '211'
    shortdesc = 'pillar.get or grains.get should be formatted differently'
    description = "pillar.get and grains.get should always be formatted " \
                  "like salt['pillar.get']('item'), grains['item1'] or " \
                  " pillar.get('item')"
    severity = 'HIGH'
    languages = [LANGUAGE_SLS, LANGUAGE_JINJA]
    tags = ['formatting', 'jinja']
    version_added = 'v0.0.10'

    bracket_regex = re.compile(r"{{( |\-|\+)?.(pillar|grains).get\[.+}}")

    def match(self, file, line):
        return self.bracket_regex.search(line)
