# -*- coding: utf-8 -*-
# Copyright (c) 2026 Warpnet B.V.

import io
import json
import unittest
from contextlib import redirect_stdout

from saltlint.formatters.codeclimate import CodeClimateFormatter, SEVERITY_MAP
from saltlint.linter.match import Match


class FakeRule:
    def __init__(self, rule_id, severity, shortdesc='short'):
        self.id = rule_id
        self.severity = severity
        self.shortdesc = shortdesc


class TestCodeClimateFormatter(unittest.TestCase):

    def _match(self, *, rule_id='204', severity='HIGH', message='boom',
               filename='states/foo.sls', linenumber=7, line='bad line'):
        return Match(linenumber, line, filename,
                     FakeRule(rule_id, severity), message=message)

    def test_format_shape(self):
        item = CodeClimateFormatter().format(self._match())
        self.assertEqual(item['description'], 'boom')
        self.assertEqual(item['check_name'], '204')
        self.assertEqual(item['severity'], 'critical')
        self.assertEqual(item['location'],
                         {'path': 'states/foo.sls', 'lines': {'begin': 7}})
        self.assertEqual(len(item['fingerprint']), 64)  # sha256 hex

    def test_severity_mapping(self):
        formatter = CodeClimateFormatter()
        for salt_sev, cc_sev in SEVERITY_MAP.items():
            with self.subTest(severity=salt_sev):
                self.assertEqual(
                    formatter.format(self._match(severity=salt_sev))['severity'],
                    cc_sev,
                )

    def test_unknown_severity_defaults_to_minor(self):
        item = CodeClimateFormatter().format(self._match(severity='WEIRD'))
        self.assertEqual(item['severity'], 'minor')

    def test_fingerprint_is_stable_and_unique(self):
        formatter = CodeClimateFormatter()
        a1 = formatter.format(self._match())['fingerprint']
        a2 = formatter.format(self._match())['fingerprint']
        b = formatter.format(self._match(linenumber=8))['fingerprint']
        self.assertEqual(a1, a2)
        self.assertNotEqual(a1, b)

    def test_process_emits_json_array(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            CodeClimateFormatter().process([self._match(), self._match(linenumber=9)])
        items = json.loads(buf.getvalue())
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]['location']['lines']['begin'], 7)
        self.assertEqual(items[1]['location']['lines']['begin'], 9)
