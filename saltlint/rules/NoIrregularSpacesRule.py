# -*- coding: utf-8 -*-

from saltlint.linter import SaltLintRule


class NoIrregularSpacesRule(SaltLintRule):
    id = '212'
    shortdesc = 'Most files should not contain irregular spaces'
    description = 'Irregular spaces can cause unexpected display issues, use spaces'
    severity = 'LOW'
    tags = ['formatting']
    version_added = 'v0.1.0'

    irregular_spaces = [
        u"\u000B",  # Line Tabulation (\v) - <VT>
        u"\u000C",  # Form Feed (\f) - <FF>
        u"\u00A0",  # No-Break Space - <NBSP>
        u"\u0085",  # Next Line
        u"\u1680",  # Ogham Space Mark
        u"\u180E",  # Mongolian Vowel Separator - <MVS>
        u"\uFEFF",  # Zero Width No-Break Space - <BOM>
        u"\u2000",  # En Quad
        u"\u2001",  # Em Quad
        u"\u2002",  # En Space - <ENSP>
        u"\u2003",  # Em Space - <EMSP>
        u"\u2004",  # Tree-Per-Em
        u"\u2005",  # Four-Per-Em
        u"\u2006",  # Six-Per-Em
        u"\u2007",  # Figure Space
        u"\u2008",  # Punctuation Space - <PUNCSP>
        u"\u2009",  # Thin Space
        u"\u200A",  # Hair Space
        u"\u200B",  # Zero Width Space - <ZWSP>
        u"\u2028",  # Line Separator
        u"\u2029",  # Paragraph Separator
        u"\u202F",  # Narrow No-Break Space
        u"\u205F",  # Medium Mathematical Space
        u"\u3000",  # Ideographic Space
        ]

    def match(self, file, line):
        res = [i for i in self.irregular_spaces if i in line]
        return len(res) != 0
