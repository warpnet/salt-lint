# -*- coding: utf-8 -*-
# Copyright (c) 2024 Anton Ovseenko

import re
from saltlint.linter.rule import Rule


class EOFRule(Rule):
    id = '220'
    shortdesc = 'Number of newline in EOF'
    description = 'There should be exactly one new line at the end of the file'
    severity = 'INFO'
    tags = ['formatting']
    version_added = 'v0.9.2'

    eof_regex = re.compile(r"\n+\Z")

    def matchtext(self, file, text):
        if len(text) == 0:
            return []

        match = self.eof_regex.search(text)
        if match:
            n = len(match.group())
            end = match.end()
            line_no = len(text[:end].splitlines())
            return [(line_no, match.group().encode(), f"{n} newline in EOF")] if n != 1 else []

        return [(len(text.splitlines()), "<End Of File>", f"No newline in EOF")]

