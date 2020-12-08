# -*- coding: utf-8 -*-
# Copyright (c) 2013-2014 Will Thames <will@thames.id.au>
# Modified work Copyright (c) 2020 Warpnet B.V.

import re
import six

from saltlint.utils import get_rule_skips_from_line, get_file_type
from saltlint.linter.match import Match
from saltlint.utils import LANGUAGE_SLS


class Rule(object):

    id = None
    shortdesc = None
    description = None
    languages = []
    match = None
    matchtext = None

    def __init__(self, config=None):
        self.config = config

    def __repr__(self):
        return self.id + ": " + self.shortdesc

    def verbose(self):
        return self.id + ": " + self.shortdesc + "\n " + self.description

    @staticmethod
    def unjinja(text):
        return re.sub(r"{{[^}]*}}", "JINJA_VAR", text)

    def is_valid_language(self, file):
        """
        Returns True if the file type is in the supported languages or no
        language is specified for the linting rule and False otherwise.

        The file type is determined based upon the file extension.
        """
        if not self.languages or get_file_type(file["path"]) in self.languages:
            return True
        return False

    def matchlines(self, file, text):
        matches = []

        if not self.match:
            return matches

        if not self.is_valid_language(file):
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

        if not self.is_valid_language(file):
            return matches

        results = self.matchtext(file, text)

        for line, section, message in results:
            matches.append(Match(line, section, file['path'], self, message))

        return matches


class DeprecationRule(Rule):
    id = None
    state = None
    deprecated_since = None

    severity = 'HIGH'
    languages = [LANGUAGE_SLS]
    tags = ['deprecation']

    @property
    def shortdesc(self):
        return "State '{}' is deprecated since SaltStack version '{}'".format(
            self.state, self.deprecated_since
        )

    @property
    def description(self):
        return self.shortdesc

    @property
    def regex(self):
        return re.compile(
            r"^\s{2}" + self.state.replace(".", r"\.") + "(?=:|$)"
        )

    def match(self, file, line):
        return self.regex.search(line)
