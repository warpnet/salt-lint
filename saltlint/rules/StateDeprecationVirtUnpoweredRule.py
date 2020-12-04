# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import DeprecationRule
from saltlint.utils import LANGUAGE_SLS


class StateDeprecationVirtUnpoweredRule(DeprecationRule):
    id = '905'
    state = 'virt.unpowered'
    deprecated_since = '2016.3.0'
    version_added = 'develop'
