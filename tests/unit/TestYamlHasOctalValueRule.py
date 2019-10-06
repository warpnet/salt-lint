# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

import unittest

from saltlint import RulesCollection
from saltlint.rules.YamlHasOctalValueRule import YamlHasOctalValueRule
from tests import RunFromText


GOOD_NUMBER_LINE = '''
testdirectory:
  file.recurse:
    - name: /tmp/directory
    - file_mode: 700
    - dir_mode: '0775'

testdirectory2:
  file.recurse:
    - name: /tmp/directory2
    - file_mode: 0
    - dir_mode: "0775"
'''

BAD_NUMBER_LINE = '''
testdirectory:
  file.recurse:
    - name: /tmp/directory
    - file_mode: 0775
    - dir_mode: 070
'''

class TestFileModeLeadingZeroRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(YamlHasOctalValueRule())

    def test_statement_positive(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(GOOD_NUMBER_LINE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(BAD_NUMBER_LINE)
        self.assertEqual(2, len(results))
