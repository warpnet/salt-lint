# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import Rule


class CmdWaitRecommendRule(Rule):
    id = '213'
    shortdesc = 'SaltStack recommends using cmd.run together with onchanges, rather than cmd.wait'
    description = 'SaltStack recommends using cmd.run together with onchanges, rather than cmd.wait'

    severity = 'LOW'
    tags = ['formatting']
    version_added = 'develop'

    regex = re.compile(r"^\s{2}cmd\.wait:(\s+)?$")

    def match(self, file, line):
        return self.regex.search(line)
