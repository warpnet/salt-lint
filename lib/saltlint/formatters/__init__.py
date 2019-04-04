# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

# Import salt libs
import salt.utils.color


class Formatter(object):

    def format(self, match, colored=False):
        formatstr = u"{0} {1}\n{2}:{3}\n{4}\n"
        if colored:
            color = salt.utils.color.get_colors()
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
            return formatstr.format(match.rule.id,
                                    match.message,
                                    match.filename,
                                    match.linenumber,
                                    match.line)
