# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.YamlHasOctalValueRule import YamlHasOctalValueRule
from tests import RunFromText


GOOD_NUMBER_STATE = '''
testdirectory:
  file.recurse:
    - name: /tmp/directory
    - file_mode: 700
    - dir_mode: '0775'

testdirectory02:
  file.recurse:
    - name: /tmp/directory02
    - file_mode: 0
    - dir_mode: "0775"

# Non-number values should be skipped, for more information see:
# https://github.com/warpnet/salt-lint/issues/68
apache_disable_default_site:
  apache_site.disabled:
    - name: 000-default

# MAC addresses shouldn't be matched, for more information see:
# https://github.com/warpnet/salt-lint/issues/202
infoblox_remove_record1:
  infoblox_host_record.absent:
    - mac: 4c:f2:d3:1b:2e:05

infoblox_remove_record2:
  infoblox_host_record.absent:
    - mac: 05:f2:d3:1b:2e:4c

# time values should not trigger this rule
some_calendar_entry:
  file.managed:
    - name: /tmp/my_unit_file
    - contents: |
        oncalendar=Sun 18:00
'''

BAD_NUMBER_STATE = '''
# Unquoted octal values with leading zero's.
testdirectory:
  file.recurse:
    - name: /tmp/directory
    - file_mode: 00
    - dir_mode: 0700

# Unquoted octal values with leading zero's followed by a YAML of Jinja
# comment.
testdirectory:
  file.recurse:
    - name: /tmp/directory
    - file_mode: 00 # COMMENT
    - dir_mode:0700{# JINJA COMMENT #}
'''

class TestYamlHasOctalValueRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(YamlHasOctalValueRule())

    def test_statement_positive(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(GOOD_NUMBER_STATE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(BAD_NUMBER_STATE)
        self.assertEqual(4, len(results))
