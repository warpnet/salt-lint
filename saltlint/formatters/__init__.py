# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Warpnet B.V.

import json


def get_colors(use=True):
    """
    Return the colors as a dict, pass False to return the colors as empty
    strings.
    """
    colors = {
        "BLACK": "\033[0;30m",
        "DARK_GRAY": "\033[1;30m",
        "RED": "\033[0;31m",
        "LIGHT_RED": "\033[1;31m",
        "GREEN": "\033[0;32m",
        "LIGHT_GREEN": "\033[1;32m",
        "BLUE": "\033[0;34m",
        "LIGHT_BLUE": "\033[1;34m",
        "MAGENTA": "\033[0;35m",
        "LIGHT_MAGENTA": "\033[1;35m",
        "CYAN": "\033[0;36m",
        "LIGHT_CYAN": "\033[1;36m",
        "LIGHT_GRAY": "\033[0;37m",
        "WHITE": "\033[1;37m",
        "DEFAULT_COLOR": "\033[00m",
        "ENDC": "\033[0m",
    }

    if not use:
        for color in colors:
            colors[color] = ''

    return colors


class BaseFormatter(object):

    def __init__(self, colored=False):
        self.colored = colored

    def process(self, matches):
        for match in matches:
            print(self.format(match))

    def format(self, match):
        raise NotImplementedError()


class Formatter(BaseFormatter):

    def format(self, match):
        formatstr = u"{0} {1}\n{2}:{3}\n{4}\n"

        color = get_colors(self.colored)
        return formatstr.format(
            u'{0}[{1}]{2}'.format(color['RED'], match.rule.id,
                                  color['ENDC']),
            u'{0}{1}{2}'.format(color['LIGHT_RED'], match.message,
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['BLUE'], match.filename,
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['CYAN'], str(match.linenumber),
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['MAGENTA'], match.line, color['ENDC'])
        )


class SeverityFormatter(BaseFormatter):

    def format(self, match):
        formatstr = u"{0} {sev} {1}\n{2}:{3}\n{4}\n"

        color = get_colors(self.colored)
        return formatstr.format(
            u'{0}[{1}]{2}'.format(color['RED'], match.rule.id,
                                  color['ENDC']),
            u'{0}{1}{2}'.format(color['LIGHT_RED'], match.message,
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['BLUE'], match.filename,
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['CYAN'], str(match.linenumber),
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['MAGENTA'], match.line, color['ENDC']),
            sev=u'{0}[{1}]{2}'.format(color['RED'], match.rule.severity,
                                      color['ENDC'])
        )


class JsonFormatter(BaseFormatter):

    def process(self, matches, *args, **kwargs):
        items = []
        for match in matches:
            items.append(self.format(match))
        print(json.dumps(items))

    def format(self, match):
        return {
            'id': match.rule.id,
            'message': match.message,
            'filename': match.filename,
            'linenumber': match.linenumber,
            'line': match.line,
            'severity': match.rule.severity,
        }
