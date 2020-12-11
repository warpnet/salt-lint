# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import unittest

from saltlint.linter.collection import RulesCollection
from saltlint.rules.FileManagedReplaceContentRule import FileManagedReplaceContentRule
from tests import RunFromText


GOOD_FILE_STATE = '''
cis_grub.cfg:
  file.managed:
    - name: /boot/grub.cfg
    - user: root
    - group: root
    - mode: '0700'
    - source: salt://grub/files/grub.cfg

cis_systemid_only_set_once:
  file.managed:
  - name: /tmp/systemid
  - user: root
  - group: root
  - replace: False
  - contents_grains: osmajorrelease

user:
  user.present:
    - name: "salt-lint"
  file.managed:
    - name: /user/salt-lint/.bashrc
    - user: root
    - group: root
    - mode: '0700'
    - contents_pillar: bashrc

cis_grub.cfg_managerights:
  file.managed:
    - name: /boot/grub.cfg
    - user: root
    - group: root
    - mode: '0700'
    - replace: False

cis_grub_permissions:
  file.managed:
    - name: /boot/grub.cfg
    - replace: false
    - user: root
    - group: root
    - mode: '0700'

# Allow options to be encapsulated by Jinja statements
cis_grub_jinja:
  file.managed:
    - name: /boot/grub.cfg
    - user: root
    - group: root
    - mode: '0700'
{% if grub.source_path is not defined %}
    - source: salt://grub/files/grub.cfg
{% else %}
    - source: {{ grub.source_path  }}
{% endif %}
'''

BAD_FILE_STATE = '''
cis_grub.cfg:
  file.managed:
  - name: /boot/grub.cfg
  - user: root
  - group: root
  - mode: '0700'

cis_systemid_only_set_once:
  file.managed:
    - name: /tmp/systemid
    - user: root
    - group: root
    - replace: True

user:
  user.present:
    - name: "salt-lint"
  file.managed:
    - name: /user/salt-lint/.bashrc
    - user: root
    - group: root
    - mode: '0700'

cis_grub_permissions:
  file.managed: # noqa: 215
    - name: /boot/grub.cfg
    - user: root
    - group: root
    - mode: '0700'
'''


class TestFileManagedReplaceContentRule(unittest.TestCase):
    collection = RulesCollection()

    def setUp(self):
        self.collection.register(FileManagedReplaceContentRule())

    def test_statement_positive(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(GOOD_FILE_STATE)
        self.assertEqual(0, len(results))

    def test_statement_negative(self):
        runner = RunFromText(self.collection)
        results = runner.run_state(BAD_FILE_STATE)
        self.assertEqual(3, len(results))

        # Check line numbers of the results
        self.assertEqual(3, results[0].linenumber)
        self.assertEqual(10, results[1].linenumber)
        self.assertEqual(19, results[2].linenumber)
