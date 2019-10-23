[![PyPI](https://img.shields.io/pypi/v/salt-lint.svg?style=for-the-badge)](https://pypi.org/project/salt-lint)
[![Travis (.org)](https://img.shields.io/travis/warpnet/salt-lint.svg?style=for-the-badge)](https://travis-ci.org/warpnet/salt-lint)
[![Coveralls](https://img.shields.io/coveralls/github/warpnet/salt-lint.svg?style=for-the-badge)](https://coveralls.io/github/warpnet/salt-lint)

# Salt-lint

`salt-lint` checks Salt state files (SLS) for practices and behavior that could potentially be improved.

The project is heavily based on [ansible-lint](https://github.com/ansible/ansible-lint), which was created by [Will Thames](https://github.com/willthames) and is now maintained as part of the [Ansible](https://www.ansible.com/) by [Red Hat](https://www.redhat.com) project.

# Installing

## Using Pip

```bash
pip install salt-lint
```

## From Source

```bash
pip install git+https://github.com/warpnet/salt-lint.git
```

# Usage

## Command Line Options

The following is the output from `salt-lint --help`, providing an overview of the basic command line options:

```bash
Usage: salt-lint [options] init.sls [state ...]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -L                    list all the rules
  -r RULESDIR           specify one or more rules directories using one or
                        more -r arguments. Any -r flags override the default
                        rules in
                        /home/roald/workspace/github.com/roaldnefs/salt-
                        lint/saltlint/rules, unless -R is also used.
  -R                    Use default rules in
                        /home/roald/workspace/github.com/roaldnefs/salt-
                        lint/saltlint/rules in addition to any extra rules
                        directories specified with -r. There is no need to
                        specify this if no -r flags are used.
  -t TAGS               only check rules whose id/tags match these values
  -T                    list all the tags
  -v                    Increase verbosity level
  -x SKIP_LIST          only check rules whose id/tags do not match these
                        values
  --nocolor             disable colored output
  --force-color         Try force colored output (relying on salt's code)
  --exclude=EXCLUDE_PATHS
                        path to directories or files to skip. This option is
                        repeatable.
  -c C                  Specify configuration file to use.  Defaults to
                        ".salt-lint"
```

## Linting Salt state files

It's important to note that `salt-lint` accepts a list of Salt state files or a list of directories.

## GitHub Action

Salt-lint is available on the GitHub [marketplace](https://github.com/marketplace/actions/salt-lint) as a GitHub Action. The `salt-lint-action` allows you to run ``salt-lint`` with no additional options.

To use the action simply add the following lines to your `.github/workflows/main.yml`.

```yaml
on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    name: Salt Lint Action
    steps:
    - uses: actions/checkout@v1
    - name: Run salt-lint
      uses: roaldnefs/salt-lint-action@master
      env:
        ACTION_STATE_NAME: init.sls
```

# Configuring

## Configuration File

Salt-lint supports local configuration via a `.salt-lint` configuration file. Salt-lint checks the working directory for the presence of this file and applies any configuration found there. The configuration file location can also be overridden via the `-c path/to/file` CLI flag.

If a value is provided on both the command line and via a configuration file, the values will be merged (if a list like **exclude_paths**), or the **True** value will be preferred, in the case of something like **quiet**.

The following values are supported, and function identically to their CLI counterparts:

```yaml
---
exclude_paths:
  - exclude_this_file
  - exclude_this_directory/
  - exclude/this/sub-directory/
skip_list:
  - 207
  - 208
tags:
  - formatting
verbosity: 1
rules:
  formatting:
    ignore: |
      ignore/this/directory/*.sls
      *.jinja
  210:
    ignore: 'exclude_this_file.sls'
```

## Pre-commit Setup

To use salt-lint with [pre-commit](https://pre-commit.com),  just add the following to your local repo's `.pre-commit-config.yaml` file. Prior to version 0.12.0 of [pre-commit](https://pre-commit.com) the file was `hooks.yaml` (now `.pre-commit-config.yaml`).

```yaml
---

# For use with pre-commit.
# See usage instructions at http://pre-commit.com

-   id: salt-lint
    name: Salt-lint
    description: This hook runs salt-lint.
    entry: salt-lint
    language: python
    files: \.(sls)$
```

# Rules

## False Positives: Skipping Rules

Some rules are bit of a rule of thumb. To skip a specific rule for a specific task, inside your state add `# noqa [rule_id]` at the end of the line. You can skip multiple rules via a space-separated list. Example:

```yaml
/tmp/testfile:
  file.managed:
    - source: salt://{{unspaced_var}}/example  # noqa: 206
```

# Authors

The project is heavily based on [ansible-lint](https://github.com/ansible/ansible-lint), with the modified work by [Warpnet B.V.](https://github.com/warpnet).  [ansible-lint](https://github.com/ansible/ansible-lint) was created by [Will Thames](https://github.com/willthames) and is now maintained as part of the [Ansible](https://www.ansible.com/) by [Red Hat](https://www.redhat.com) project.
