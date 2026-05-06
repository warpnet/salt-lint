# -*- coding: utf-8 -*-
# Copyright (c) 2026 Warpnet B.V.

import hashlib
import json

from saltlint.formatters.base import BaseFormatter


SEVERITY_MAP = {
    'INFO': 'info',
    'VERY_LOW': 'minor',
    'LOW': 'minor',
    'MEDIUM': 'major',
    'HIGH': 'critical',
}


class CodeClimateFormatter(BaseFormatter):
    def process(self, problems, *args, **kwargs):
        items = [self.format(p) for p in problems]
        print(json.dumps(items))

    def format(self, problem):
        identifier = "{}:{}:{}:{}".format(
            problem.rule.id,
            problem.filename,
            problem.linenumber,
            problem.line,
        )
        fingerprint = hashlib.sha256(identifier.encode('utf-8')).hexdigest()
        return {
            'description': problem.message,
            'check_name': problem.rule.id,
            'fingerprint': fingerprint,
            'severity': SEVERITY_MAP.get(problem.rule.severity, 'minor'),
            'location': {
                'path': problem.filename,
                'lines': {'begin': problem.linenumber},
            },
        }
