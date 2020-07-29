# -*- coding: utf-8 -*-
# Added bij Chris van Breeden, Copyright (c) 2020
#

import re
import os
from saltlint.linter import SaltLintRule


class JinjaTemplateHasRightExtensionRule(SaltLintRule):
    id = '213'
    shortdesc = 'Jinja templates should have the correct file extension'
    description = 'Jinja templates should have the correct file extension'
    severity = 'LOW'
    tags = ['formatting', 'jinja']
    version_added = 'v0.0.1'
    right_extensions = ['.sls', '.jinja', '.jinja2', '.j2']
    done = []  # already noticed path list

    jinja_syntax = re.compile(r"{{|{%-")

    def match(self, file, line):
        path = file['path']
        ext = os.path.splitext(path)
        if ext[1] not in self.right_extensions and path not in self.done:
            has_jinja = self.jinja_syntax.search(line)
            if has_jinja:
                self.done.append(path)
                return True

        return False
