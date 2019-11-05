# -*- coding: utf-8 -*-
# Copyright (c) 2013-2014 Will Thames <will@thames.id.au>
# Modified work Copyright (c) 2019 Warpnet B.V.

import glob
import imp
import os


def load_plugins(directory, config):
    result = []
    fh = None

    for pluginfile in glob.glob(os.path.join(directory, '[A-Za-z]*.py')):

        pluginname = os.path.basename(pluginfile.replace('.py', ''))
        try:
            fh, filename, desc = imp.find_module(pluginname, [directory])
            mod = imp.load_module(pluginname, fh, filename, desc)
            obj = getattr(mod, pluginname)(config)
            result.append(obj)
        finally:
            if fh:
                fh.close()
    return result


def get_rule_skips_from_line(line):
    rule_id_list = []
    if '# noqa' in line:
        noqa_text = line.split('# noqa')[1]
        rule_id_list = noqa_text.split()
    return rule_id_list
