# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

from saltlint.linter import SaltLintRule
from salt.exceptions import SaltRenderError
import salt.loader
import salt.config
import os

class StateCanBeRendered(SaltLintRule):
    id = '218'
    shortdesc = 'Rendered sls file should be valid.'
    description = 'Rendered sls file should be valid.'
    severity = 'HIGH'
    tags = ['formatting']
    version_added = 'develop'

    def matchtext(self, file, text):
        __opts__ = salt.config.minion_config('/etc/salt/minion')
        __grains__ = salt.loader.grains(__opts__)
        __opts__['grains'] = __grains__
        __opts__['file_client'] = 'local'
        __utils__ = salt.loader.utils(__opts__)
        __salt__ = salt.loader.minion_mods(__opts__, utils=__utils__)

        try:
            if os.path.isabs(file['path']):
                __salt__['slsutil.renderer'](file['path'])
            else:
                __salt__['slsutil.renderer'](os.path.realpath(file['path']))
        except SaltRenderError as err:
            return [(1, err, None)]

        return []
