# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import Rule
from saltlint.utils import get_rule_skips_from_text
from saltlint.utils import LANGUAGE_SLS


class CronStateHasIdentifierRule(Rule):
    id = '801'
    shortdesc = 'It is recommended to use an identifier with cron.present'
    description = 'It is recommended to use an identifier with cron.present'

    severity: 'LOW'
    languages = [LANGUAGE_SLS]
    tags = ['recommendation']
    version_added = 'develop'

    regex = re.compile(r"^\s{2}cron\.present:.*(?:\n\s{4}.+)*", re.MULTILINE)
    regex_identifier = re.compile(r"^\s{4}-\sidentifier:.+$", re.MULTILINE)

    def matchtext(self, file, text):
        results = []

        # Find all cron.present states in the specified sls file
        for match in re.finditer(self.regex, text):
            # Check if regex_identifier is found within each state
            if re.search(self.regex_identifier, match.group(0)):
                continue

            # Get the location of the regex match
            start = match.start()
            end = match.end()

            # Get the line number of the first character
            lines = text[:start].splitlines()
            line_no = len(lines) + 1

            # Skip result if noqa for this rule ID is found in section
            section = text[start:end]
            if self.id in get_rule_skips_from_text(section):
                continue

            # Append the match to the results
            results.append((line_no, section.splitlines()[0], self.shortdesc))

        return results
