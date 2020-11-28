# -*- coding: utf-8 -*-
# Copyright (c) 2013-2014 Will Thames <will@thames.id.au>
# Modified work Copyright (c) 2020 Warpnet B.V.

import re
import six

from saltlint.utils import get_rule_skips_from_line
from saltlint.linter import Match


class Rule(object):

    def __init__(self, config=None):
        self.config = config

    def __repr__(self):
        return self.id + ": " + self.shortdesc

    def verbose(self):
        return self.id + ": " + self.shortdesc + "\n " + self.description

    match = None
    matchtext = None

    @staticmethod
    def unjinja(text):
        return re.sub(r"{{[^}]*}}", "JINJA_VAR", text)

    def matchlines(self, file, text):
        matches = []
        if not self.match:
            return matches

        # arrays are 0-based, line numbers are 1-based
        # so use prev_line_no as the counter
        for (prev_line_no, line) in enumerate(text.split("\n")):
            if line.lstrip().startswith('#'):
                continue

            rule_id_list = get_rule_skips_from_line(line)
            if self.id in rule_id_list:
                continue

            result = self.match(file, line)
            if not result:
                continue
            message = None
            if isinstance(result, six.string_types):
                message = result
            matches.append(Match(prev_line_no+1, line,
                                 file['path'], self, message))

        return matches

    def matchfulltext(self, file, text):
        matches = []
        if not self.matchtext:
            return matches

        results = self.matchtext(file, text)

        for line, section, message in results:
            matches.append(Match(line, section, file['path'], self, message))

        return matches
