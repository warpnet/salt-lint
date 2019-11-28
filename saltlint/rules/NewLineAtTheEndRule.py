# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

from saltlint.linter import SaltLintRule


class NewLineAtTheEndRule(SaltLintRule):
    id = '216'
    shortdesc = 'The POSIX standard requires the last line to be a new line character.'
    description = 'The POSIX standard requires the last line to be a new line character.'
    severity = 'LOW'
    tags = ['formatting']
    version_added = 'develop'

    def matchtext(self, _, text):
        lines = text.splitlines()
        results = []
        if lines and lines[-1] != '':
            results.append((len(lines), lines[-1], None))

        return results
