# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

import re
from saltlint.linter.rule import DeprecationRule
from saltlint.utils import LANGUAGE_SLS


class StateDeprecationElasticsearchIndexRule(DeprecationRule):
    id = '902'
    state = 'elasticsearch_index.absent'
    deprecated_since = '2017.7.0'
    version_added = 'develop'
