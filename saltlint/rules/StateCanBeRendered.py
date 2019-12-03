# -*- coding: utf-8 -*-
# Copyright (c) 2019 Dawid Malinowski <dawidmalina@gmail.com>

import os
import salt.loader
import salt.config
from salt.exceptions import SaltRenderError
from saltlint.linter import SaltLintRule


class StateCanBeRendered(SaltLintRule):
    id = '218'
    shortdesc = 'Provided sls file must be renderable.'
    description = 'Provided sls file must be renderable.'
    severity = 'HIGH'
    tags = ['formatting', 'jinja']
    version_added = 'develop'

    def matchtext(self, file, _):
        __opts__ = salt.config.minion_config('/etc/salt/minion')
        __grains__ = salt.loader.grains(__opts__)
        __opts__['grains'] = __grains__
        __opts__['file_client'] = 'local'
        __opts__['cachedir'] = '/tmp/_cache'
        __utils__ = salt.loader.utils(__opts__)
        __salt__ = salt.loader.minion_mods(__opts__, utils=__utils__)

        try:
            if os.path.isabs(file['path']):
                __salt__['slsutil.renderer'](file['path'])
            else:
                __salt__['slsutil.renderer'](os.path.realpath(file['path']))
        except SaltRenderError as err:
            return [('', err, None)]

        return []
