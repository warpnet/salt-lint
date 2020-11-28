# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import Rule


class CmdRunQuietRule(Rule):
    id = '901'
    shortdesc = 'Using the quiet argument with cmd.run is deprecated. Use output_loglevel: quiet'
    description = 'Using the quiet argument with cmd.run is deprecated. Use output_loglevel: quiet'

    severity = 'HIGH'
    tags = ['deprecation']
    version_added = 'develop'

    regex = re.compile(r"^\s{2}cmd\.run:(?:\n.+)+\n^\s{4}- quiet\s?.*", re.MULTILINE)

    def matchtext(self, file, text):
        results = []

        for match in re.finditer(self.regex, text):
            # Get the location of the last character in the regex match
            end = match.end()
            # Get the line number of the last character
            lines = text[:end].splitlines()
            line_no = len(lines)
            # Append the match to the results
            results.append((line_no, lines[-1], self.shortdesc))

        return results

