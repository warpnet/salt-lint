# -*- coding: utf-8 -*-
# Copyright (c) 2016 Will Thames and contributors
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2021 Warpnet B.V.
# Modified work Copyright (c) 2021 Yury Bushmelev

import re
from saltlint.linter.rule import TypographicalErrorRule


class TypoContentsRule(TypographicalErrorRule):
    id = '218'
    shortdesc = '"content" looks like a typo. Did you mean "contents"?'
    description = '"content" looks like a typo. Did you mean "contents"?'
    version_added = 'v0.6.0'
    regex = re.compile(r"^\s+- content(|_pillar|_grains|_newline|_delimiter):")
