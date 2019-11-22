# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Warpnet B.V.

import json

# Import salt libs
try:
    import salt.utils.color as saltcolor
except ImportError:
    import salt.utils as saltcolor


class Formatter(object):

    def process(self, matches, colored=False):
        for match in matches:
            print(self.format(match, colored))

    def format(self, match, colored=False):
        formatstr = u"{0} {1}\n{2}:{3}\n{4}\n"
        if colored:
            color = saltcolor.get_colors()
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
        else:
            return formatstr.format(
                u'[{0}]'.format(match.rule.id),
                match.message,
                match.filename,
                match.linenumber,
                match.line)


class SeverityFormatter(object):
    def process(self, matches, colored=False):
        for match in matches:
            print(self.format(match, colored))

    def format(self, match, colored=False):
        formatstr = u"{0} {sev} {1}\n{2}:{3}\n{4}\n"

        if colored:
            color = saltcolor.get_colors()
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
        else:
            return formatstr.format(
                u'[{0}]'.format(match.rule.id),
                match.message,
                match.filename,
                match.linenumber,
                match.line,
                sev=u'[{0}]'.format(match.rule.severity))


class JsonFormatter(object):

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
