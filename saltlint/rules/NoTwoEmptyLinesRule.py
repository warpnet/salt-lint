# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

from saltlint.linter import SaltLintRule


class NoTwoEmptyLinesRule(SaltLintRule):
    id = '217'
    shortdesc = 'Files should not contain two consecutive blank lines.'
    description = 'Files should not contain two consecutive blank lines.'
    severity = 'LOW'
    tags = ['formatting']
    version_added = 'v0.1.1'

    def matchtext(self, _, text):
        lines = text.splitlines()
        results = []
        for index, line in enumerate(lines):
            if line == '':
                if lines[index-1] == '':
                    results.append((index, '', None))

        return results
