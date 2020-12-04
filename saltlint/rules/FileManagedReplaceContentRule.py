# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import Rule
from saltlint.utils import get_rule_skips_from_text
from saltlint.utils import LANGUAGE_SLS


class FileManagedReplaceContentRule(Rule):
    id = '215'
    shortdesc = "Using 'replace: False' is required when not specifying content"
    description = "Using 'replace: False' is required when not specifying content"

    severity = 'HIGH'
    languages = [LANGUAGE_SLS]
    tags = ['formatting']
    version_added = 'develop'

    # Find the full file.managed state
    regex = re.compile(r"^\s{2}file\.managed:.*(?:\n\s{4}.+)*", re.MULTILINE)
    # Regex for finding the content source option
    regex_options= re.compile(
        r"^\s{4}-\s(?:source:|contents:|contents_pillar:|contents_grains:|replace:\s[F|f]alse).*$",
        re.MULTILINE
    )

    def matchtext(self, file, text):
        results = []

        # Find all file.managed states in the specified sls file
        for match in re.finditer(self.regex, text):
            # Continue if the file.managed state includes a content source
            # or replace is set to False
            if re.search(self.regex_options, match.group(0)):
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
