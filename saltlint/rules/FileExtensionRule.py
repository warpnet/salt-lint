# -*- coding: utf-8 -*-
# Copyright (c) 2016 Tsukinowa Inc. <info@tsukinowa.jp>
# Copyright (c) 2018 Ansible Project
# Modified work Copyright (c) 2019 Warpnet B.V.

from saltlint.linter import SaltLintRule

import os


class FileExtensionRule(SaltLintRule):
    id = '205'
    shortdesc = 'Use ".sls" as a Salt State file extension'
    description = 'Salt State files should have the ".sls" extension'
    severity = 'MEDIUM'
    tags = ['formatting']
    done = []  # already noticed path list
    version_added = 'v0.0.1'

    def match(self, file, line):
        if file['type'] != 'state':
            return False

        path = file['path']
        ext = os.path.splitext(path)
        if ext[1] not in ['.sls'] and path not in self.done:
            self.done.append(path)
            return True
        return False
