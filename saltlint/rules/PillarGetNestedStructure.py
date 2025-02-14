# -*- coding: utf-8 -*-
# Copyright (c) 2025 IT Services, Stockholm University

import re
from saltlint.linter.rule import JinjaRule


class PillarGetNestedStructure(JinjaRule):
    id = '220'
    shortdesc = 'Trying to get nested pillar structures with .get() or []'
    description = "Using pillar.get() or pillar[] to get a:nested:structure "
    "doesn't work. It tries to get a key named 'a:nested:structure' instead "
    "of the value of ['a']['nested']['structure'] in the dict. See "
    "https://docs.saltproject.io/salt/user-guide/en/latest/topics/pillar.html#rendering-pillar"
    severity = 'HIGH'
    version_added = 'develop'

    regex = re.compile(r"pillar.get\(.+?:.+?\)|pillar\[.+?:.+?\]")

    def match(self, file, text):
        return self.regex.search(text)
