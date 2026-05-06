# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import Rule
from saltlint.utils import get_rule_skips_from_text
from saltlint.utils import LANGUAGE_SLS


class CronIdRule(Rule):
    id = '801'
    shortdesc = 'cron.present should have an identifier'
    description = 'cron.present should have an identifier'

    severity = 'MEDIUM'
    languages = [LANGUAGE_SLS]
    tags = ['reccomendation']
    version_added = 'v0.9.4'

    regex = re.compile(r"""^\s{2}cron\.present:\n(?!^\s{2,4}- identifier:\n)(?:^\s{2,4}- .+\n)+""",
                       re.MULTILINE)

    def matchtext(self, file, text):
        results = []

        for match in re.finditer(self.regex, text):
            # Get the location of the regex match
            start = match.start()
            end = match.end()

            # Get the line number of the last character
            lines = text[:end].splitlines()
            line_no = len(lines)

            # Skip result if noqa for this rule ID is found in section
            section = text[start:end]
            if self.id in get_rule_skips_from_text(section):
                continue

            # check if block contains identifier
            has_identifier = False
            if "\n  - identifier:" in section or "\n    - identifier:" in section:
                has_identifier = True
            if not has_identifier:
                results.append((line_no, lines[-1], self.shortdesc))

        return results
