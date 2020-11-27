# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Warpnet B.V.

import json


class BaseFormatter(object):

    def __init__(self, colored=False):
        self.colored = colored

    def process(self, problems):
        for problem in problems:
            print(self.format(problem))

    def format(self, problem):
        raise NotImplementedError()


class Formatter(BaseFormatter):

    def format(self, problem):
        formatstr = u"{0} {1}\n{2}:{3}\n{4}\n"

        color = get_colors(self.colored)
        return formatstr.format(
            u'{0}[{1}]{2}'.format(color['RED'], problem.rule.id,
                                  color['ENDC']),
            u'{0}{1}{2}'.format(color['LIGHT_RED'], problem.message,
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['BLUE'], problem.filename,
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['CYAN'], str(problem.linenumber),
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['MAGENTA'], problem.line, color['ENDC'])
        )


class SeverityFormatter(BaseFormatter):

    def format(self, problem):
        formatstr = u"{0} {sev} {1}\n{2}:{3}\n{4}\n"

        color = get_colors(self.colored)
        return formatstr.format(
            u'{0}[{1}]{2}'.format(color['RED'], problem.rule.id,
                                  color['ENDC']),
            u'{0}{1}{2}'.format(color['LIGHT_RED'], problem.message,
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['BLUE'], problem.filename,
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['CYAN'], str(problem.linenumber),
                                color['ENDC']),
            u'{0}{1}{2}'.format(color['MAGENTA'], problem.line, color['ENDC']),
            sev=u'{0}[{1}]{2}'.format(color['RED'], problem.rule.severity,
                                      color['ENDC'])
        )


class JsonFormatter(BaseFormatter):
    def process(self, problems, *args, **kwargs):
        items = []
        for problem in problems:
            items.append(self.format(problem))
        print(json.dumps(items))

    def format(self, problem):
        return {
            'id': problem.rule.id,
            'message': problem.message,
            'filename': problem.filename,
            'linenumber': problem.linenumber,
            'line': problem.line,
            'severity': problem.rule.severity,
        }


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
