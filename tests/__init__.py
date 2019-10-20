# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

import tempfile

from saltlint.linter import Runner
from saltlint.config import SaltLintConfig


class RunFromText(object):
    """Use Runner on temporary files created from unittest text snippets."""

    def __init__(self, collection):
        self.collection = collection

    def _call_runner(self, path):
        runner = Runner(self.collection, path, SaltLintConfig())
        return runner.run()

    def run_state(self, state_text):
        with tempfile.NamedTemporaryFile() as fp:
            fp.write(state_text.encode())
            fp.seek(0)
            results = self._call_runner(fp.name)
        return results
