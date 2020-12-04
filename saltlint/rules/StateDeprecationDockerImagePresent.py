# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import DeprecationRule
from saltlint.utils import LANGUAGE_SLS


class StateDeprecationDockerImagePresent(DeprecationRule):
    id = '908'
    state = 'docker.image_present'
    deprecated_since = '2017.7.0'
    version_added = 'develop'
