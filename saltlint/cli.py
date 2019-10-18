# -*- coding: utf-8 -*-
# Copyright (c) 2013-2014 Will Thames <will@thames.id.au>
# Modified work Copyright (c) 2019 Roald Nefs

from __future__ import print_function

import optparse
import sys

from saltlint import formatters, NAME, VERSION
from saltlint.linter import default_rulesdir
from saltlint.config import SaltLintConfig, SaltLintConfigError
from saltlint.linter import RulesCollection, Runner


def run():
    formatter = formatters.Formatter()

    parser = optparse.OptionParser("%prog [options] init.sls [state ...]",
                                   version='{} {}'.format(NAME, VERSION))

    parser.add_option('-L', dest='listrules', default=False,
                      action='store_true', help="list all the rules")
    parser.add_option('-r', action='append', dest='rulesdir',
                      default=[], type='str',
                      help="specify one or more rules directories using "
                           "one or more -r arguments. Any -r flags override "
                           "the default rules in %s, unless -R is also used."
                           % default_rulesdir)
    parser.add_option('-R', action='store_true',
                      default=False,
                      dest='use_default_rules',
                      help="Use default rules in %s in addition to any extra "
                           "rules directories specified with -r. There is "
                           "no need to specify this if no -r flags are used."
                           % default_rulesdir)
    parser.add_option('-t', dest='tags',
                      action='append',
                      default=[],
                      help="only check rules whose id/tags match these values")
    parser.add_option('-T', dest='listtags', action='store_true',
                      help="list all the tags")
    parser.add_option('-v', dest='verbosity', action='count',
                      help="Increase verbosity level",
                      default=0)
    parser.add_option('-x', dest='skip_list', default=[], action='append',
                      help="only check rules whose id/tags do not " +
                      "match these values")
    parser.add_option('--nocolor', dest='colored',
                      default=hasattr(sys.stdout, 'isatty') and sys.stdout.isatty(),
                      action='store_false',
                      help="disable colored output")
    parser.add_option('--force-color', dest='colored',
                      action='store_true',
                      help="Try force colored output (relying on salt's code)")
    parser.add_option('--exclude', dest='exclude_paths', action='append',
                      help='path to directories or files to skip. This option'
                           ' is repeatable.',
                      default=[])
    parser.add_option('-c', help='Specify configuration file to use.  Defaults to ".salt-lint"')
    options, args = parser.parse_args(sys.argv[1:])

    # Read, parse and validate the configration
    try:
        config = SaltLintConfig(options)
    except SaltLintConfigError as exc:
        print(exc)
        return 2

    # Show a help message on the screen
    if len(args) == 0 and not (options.listrules or options.listtags):
        parser.print_help(file=sys.stderr)
        return 1

    # Collect the rules from the configution
    rules = RulesCollection(config)
    for rulesdir in config.rulesdirs:
        rules.extend(RulesCollection.create_from_directory(rulesdir, config))

    # Show the rules listing
    if options.listrules:
        print(rules)
        return 0

    # Show the tags listing
    if options.listtags:
        print(rules.listtags())
        return 0

    states = set(args)
    matches = list()
    checked_files = set()
    for state in states:
        runner = Runner(rules, state, config, checked_files)
        matches.extend(runner.run())

    # Sort the matches
    matches.sort(key=lambda x: (x.filename, x.linenumber, x.rule.id))

    # Show the matches on the screen
    for match in matches:
        print(formatter.format(match, config.colored))

    # Return the exit code
    if len(matches):
        return 2
    else:
        return 0
