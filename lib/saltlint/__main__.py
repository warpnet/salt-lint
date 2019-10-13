# !/usr/bin/env python

# Copyright (c) 2013-2014 Will Thames <will@thames.id.au>
# Modified work Copyright (c) 2019 Roald Nefs

from __future__ import print_function

import errno
import optparse
import sys

import saltlint
import saltlint.formatters as formatters
import six
from saltlint import RulesCollection
from saltlint.version import __version__
import yaml
import os


def load_config(config_file):
    config_path = config_file if config_file else ".salt-lint"

    if os.path.exists(config_path):
        with open(config_path, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLERROR:
                pass

    return None


def main():

    formatter = formatters.Formatter()

    parser = optparse.OptionParser("%prog [options] init.sls [state ...]",
                                   version="%prog " + __version__)

    parser.add_option('-L', dest='listrules', default=False,
                      action='store_true', help="list all the rules")

    parser.add_option('-t', dest='tags',
                      action='append',
                      default=[],
                      help="only check rules whose id/tags match these values")
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

    parser.add_option('-r', action='append', dest='rulesdir',
                      default=[], type='str',
                      help="specify one or more rules directories using "
                           "one or more -r arguments. Any -r flags override "
                           "the default rules in %s, unless -R is also used."
                           % saltlint.default_rulesdir)
    parser.add_option('-R', action='store_true',
                      default=False,
                      dest='use_default_rules',
                      help="Use default rules in %s in addition to any extra "
                           "rules directories specified with -r. There is "
                           "no need to specify this if no -r flags are used"
                           % saltlint.default_rulesdir)
    options, args = parser.parse_args(sys.argv[1:])

    config = load_config(options.c)

    if config:
        # TODO parse configuration options

        if 'verbosity' in config:
            options.verbosity = options.verbosity + config['verbosity']

        if 'exclude_paths' in config:
            options.exclude_paths = options.exclude_paths + config['exclude_paths']

        if 'skip_list' in config:
            options.skip_list = options.skip_list + config['skip_list']

        if 'tags' in config:
            options.tags = options.tags + config['tags']

        if 'use_default_rules' in config:
            options.use_default_rules = options.use_default_rules or config['use_default_rules']

        if 'rulesdir' in config:
            options.rulesdir = options.rulesdir + config['rulesdir']

    if len(args) == 0 and not (options.listrules):
        parser.print_help(file=sys.stderr)
        return 1

    if options.use_default_rules:
        rulesdirs = options.rulesdir + [saltlint.default_rulesdir]
    else:
        rulesdirs = options.rulesdir or [saltlint.default_rulesdir]

    rules = RulesCollection()
    for rulesdir in rulesdirs:
        rules.extend(RulesCollection.create_from_directory(rulesdir))

    if options.listrules:
        print(rules)
        return 0

    if isinstance(options.tags, six.string_types):
        options.tags = options.tags.split(',')

    skip = set()
    for s in options.skip_list:
        skip.update(str(s).split(','))
    options.skip_list = frozenset(skip)

    states = set(args)
    matches = list()
    checked_files = set()
    for state in states:
        runner = saltlint.Runner(rules, state, options.tags,
                                 options.skip_list, options.exclude_paths,
                                 options.verbosity, checked_files)
        matches.extend(runner.run())

    matches.sort(key=lambda x: (x.filename, x.linenumber, x.rule.id))

    for match in matches:
        print(formatter.format(match, options.colored))

    if len(matches):
        return 2
    else:
        return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except IOError as exc:
        if exc.errno != errno.EPIPE:
            raise
    except RuntimeError as e:
        raise SystemExit(str(e))
