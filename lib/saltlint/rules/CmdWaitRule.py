# Copyright (c) 2016, Tsukinowa Inc. <info@tsukinowa.jp>
# Copyright (c) 2018, Ansible Project
# Modified work Copyright (c) 2019 Roald Nefs

from saltlint import SaltLintRule

import os
import six


class CmdWaitRule(SaltLintRule):
    id = '100'
    shortdesc = 'Use ``cmd.run`` together with ``onchanges`` instead of ``cmd.wait``.'
    description = 'Use ``cmd.run`` together with ``onchanges`` instead of ``cmd.wait``.'
    severity = 'HIGH'
    tags = ['formatting']
    version_added = 'develop'

    def matchyaml(self, file, yaml):
        results = []

        for state_id, state in six.iteritems(yaml):
            if isinstance(state, dict):
                for key, value in six.iteritems(state):
                    if key == 'cmd.wait':
                        results.append(('In state with ID: {}'.format(state_id), self.description))
                        print('cmd.wait FOUND!')

                    if key == 'cmd':
                        if isinstance(value, list):
                            for entry in value:
                                if entry == 'wait':
                                    results.append((('In state with ID: {}'.format(state_id), self.description))

        return results