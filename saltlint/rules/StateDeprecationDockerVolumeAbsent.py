# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import DeprecationRule
from saltlint.utils import LANGUAGE_SLS


class StateDeprecationDockerVolumeAbsent(DeprecationRule):
    id = '914'
    state = 'docker.volume_absent'
    deprecated_since = '2017.7.0'
    version_added = 'develop'
