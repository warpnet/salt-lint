# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2019 Warpnet B.V.

from saltlint.linter import SaltLintRule
import re


class JinjaPillarGrainsGetFormatRule(SaltLintRule):
    id = '211'
    shortdesc = 'pillar.get or grains.get should be formatted differently'
    description = "pillar.get and grains.get should always be formatted " \
                  "like salt['pillar.get']('item'), grains['item1'] or " \
                  " pillar.get('item')"
    severity = 'HIGH'
    tags = ['formatting', 'jinja']
    version_added = 'v0.0.10'

    bracket_regex = re.compile(r"{{( |\-|\+)?.(pillar|grains).get\[.+}}")

    def match(self, file, line):
        return self.bracket_regex.search(line)
