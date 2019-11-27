# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

import re
from saltlint.linter import SaltLintRule


class ColonFormatRule(SaltLintRule):
    id = '214'
    shortdesc = 'The line should have an proper colons formatting.'
    description = 'The line should have an proper colons formatting.'
    severity = 'MEDIUM'
    tags = ['formatting']
    version_added = 'develop'

    regex = re.compile(r"([\s]{1,}:)|((:\{)(?!\{))|(:\[)")

    def match(self, file, line):
        # pylint: disable=unused-argument
        return self.regex.search(line)
