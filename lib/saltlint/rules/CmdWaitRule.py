# Copyright (c) 2019 Roald Nefs

from saltlint import SaltLintRule

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

        if not isinstance(yaml, dict):
            return results

        # Loop over the individual states
        for state_id, state in six.iteritems(yaml):
            # Skip entries that aren't a dictionary
            if not isinstance(state, dict):
                continue

            # Loop over key, value pairs in the state
            for key, value in six.iteritems(state):

                # Match inline function
                if key == 'cmd.wait':
                    results.append((
                        'In state with ID: {}'.format(state_id),
                        self.description)
                    )

                # Match standard state declaration
                if key == 'cmd' and isinstance(value, list):
                    # Look for the 'wait' function
                    if 'wait' in value:
                        results.append((
                            'In state with ID: {}'.format(state_id),
                            self.description)
                        )

        return results
