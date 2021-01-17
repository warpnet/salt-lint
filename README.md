# salt-lint

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/salt-lint?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/salt-lint/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/salt-lint?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/salt-lint/)
[![PyPI - Format](https://img.shields.io/pypi/format/salt-lint?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/salt-lint/)
[![License](https://img.shields.io/github/license/warpnet/salt-lint?style=for-the-badge)](https://raw.githubusercontent.com/warpnet/salt-lint/main/LICENSE)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/warpnet/salt-lint/tests?label=CI&logo=github&style=for-the-badge)](https://github.com/warpnet/salt-lint/actions)
[![GitHub contributors](https://img.shields.io/github/contributors/warpnet/salt-lint?logo=github&style=for-the-badge)](https://github.com/warpnet/salt-lint/graphs/contributors)


`salt-lint` checks Salt State files (SLS) for best practices and behavior that could potentially be improved.

The project is heavily based on [ansible-lint](https://github.com/ansible/ansible-lint), which was created by [Will Thames](https://github.com/willthames) and is now maintained as part of the [Ansible](https://www.ansible.com/) by [Red Hat](https://www.redhat.com) project.

## Demo

[![salt-lint demo](https://raw.githubusercontent.com/warpnet/salt-lint/main/demo.gif?raw=true)](https://asciinema.org/a/377244)

## Installing

### Using Pip

```bash
pip install salt-lint
```

### From Source

```bash
pip install git+https://github.com/warpnet/salt-lint.git
```

## Usage

### Command Line Options

The following is the output from `salt-lint --help`, providing an overview of the basic command line options:

```bash
usage: salt-lint [-h] [--version] [-L] [-r RULESDIR] [-R] [-t TAGS] [-T] [-v] [-x SKIP_LIST] [--nocolor] [--force-color]
                 [--exclude EXCLUDE_PATHS] [--json] [--severity] [-c C]
                 files [files ...]

positional arguments:
  files                 One or more files or paths.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -L                    list all the rules
  -r RULESDIR           specify one or more rules directories using one or more -r arguments. Any -r flags
                        override the default rules in /path/to/salt-lint/saltlint/rules, unless -R is also used.
  -R                    Use default rules in /path/to/salt-lint/saltlint/rules in addition to any extra rules
                        directories specified with -r. There is no need to specify this if no -r flags are used.
  -t TAGS               only check rules whose id/tags match these values
  -T                    list all the tags
  -v                    Increase verbosity level
  -x SKIP_LIST          only check rules whose id/tags do not match these values
  --nocolor, --nocolour
                        disable colored output
  --force-color, --force-colour
                        Try force colored output (relying on salt's code)
  --exclude EXCLUDE_PATHS
                        path to directories or files to skip. This option is repeatable.
  --json                parse the output as JSON
  --severity            add the severity to the standard output
  -c C                  Specify configuration file to use. Defaults to ".salt-lint"
```

### Linting Salt State files

It's important to note that `salt-lint` accepts a list of Salt State files or a list of directories.

### Docker & Podman

salt-lint is available on [Dockerhub](https://hub.docker.com/r/warpnetbv/salt-lint).

Example usage:

```bash
docker run -v $(pwd):/data:ro --entrypoint=/bin/bash -it warpnetbv/salt-lint:latest -c 'find /data -type f -name "*.sls" | xargs --no-run-if-empty salt-lint'
```

On a system with SELinux, change `:ro` to `:Z`. Example below uses podman:

```bash
podman run -v $(pwd):/data:Z --entrypoint=/bin/bash -it warpnetbv/salt-lint:latest -c 'find /data -type f -name "*.sls" | xargs --no-run-if-empty salt-lint'
```

### GitHub Action

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

## Configuring

### Configuration File

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
severity: True
```

### Pre-commit Setup

To use salt-lint with [pre-commit](https://pre-commit.com),  just add the following to your local repo's `.pre-commit-config.yaml` file. Prior to version 0.12.0 of [pre-commit](https://pre-commit.com) the file was `hooks.yaml` (now `.pre-commit-config.yaml`).

```yaml
---

# For use with pre-commit.
# See usage instructions at http://pre-commit.com

-   repo: https://github.com/warpnet/salt-lint
    rev: v0.5.0
    hooks:
      - id: salt-lint
```

Optionally override the default file selection as follows:

```yaml
      ...
      - id: salt-lint
        files: \.(sls|jinja|tmpl)$
```

## Rules

### List of rules

#### Formatting

Disable formatting checks using `-x formatting`

Rule | Description
:-:|:--
[201](https://github.com/warpnet/salt-lint/wiki/201) | Trailing whitespace
[202](https://github.com/warpnet/salt-lint/wiki/202) | Jinja statement should have spaces before and after: `{% statement %}`
[203](https://github.com/warpnet/salt-lint/wiki/203) | Most files should not contain tabs
[204](https://github.com/warpnet/salt-lint/wiki/204) | Lines should be no longer than 160 chars
[205](https://github.com/warpnet/salt-lint/wiki/205) | Use ".sls" as a Salt State file extension
[206](https://github.com/warpnet/salt-lint/wiki/206) | Jinja variables should have spaces before and after `{{ var_name }}`
[207](https://github.com/warpnet/salt-lint/wiki/207) | File modes should always be encapsulated in quotation marks
[208](https://github.com/warpnet/salt-lint/wiki/208) | File modes should always contain a leading zero
[209](https://github.com/warpnet/salt-lint/wiki/209) | Jinja comment should have spaces before and after: `{# comment #}`
[210](https://github.com/warpnet/salt-lint/wiki/210) | Numbers that start with `0` should always be encapsulated in quotation marks
[211](https://github.com/warpnet/salt-lint/wiki/211) | `pillar.get` or `grains.get` should be formatted differently
[212](https://github.com/warpnet/salt-lint/wiki/212) | Most files should not contain irregular spaces
[213](https://github.com/warpnet/salt-lint/wiki/213) | SaltStack recommends using `cmd.run` together with `onchanges`, rather than `cmd.wait`
[214](https://github.com/warpnet/salt-lint/wiki/214) | SLS file with a period in the name (besides the suffix period) can not be referenced

#### Jinja

Disable jinja checks using `-x jinja`

Rule | Description
:-:|:--
[202](https://github.com/warpnet/salt-lint/wiki/202) | Jinja statement should have spaces before and after: `{% statement %}`
[206](https://github.com/warpnet/salt-lint/wiki/206) | Jinja variables should have spaces before and after `{{ var_name }}`
[209](https://github.com/warpnet/salt-lint/wiki/209) | Jinja comment should have spaces before and after: `{# comment #}`
[211](https://github.com/warpnet/salt-lint/wiki/211) | `pillar.get` or `grains.get` should be formatted differently

#### Deprecations

Disable deprecation checks using `-x deprecation`

Rule | Description
:-:|:--
[901](https://github.com/warpnet/salt-lint/wiki/901) | Using the `quiet` argument with `cmd.run` is deprecated. Use `output_loglevel: quiet`

### False Positives: Skipping Rules

Some rules are bit of a rule of thumb. To skip a specific rule for a specific task, inside your state add `# noqa [rule_id]` at the end of the line. You can skip multiple rules via a space-separated list. Example:

```yaml
/tmp/testfile:
  file.managed:
    - source: salt://{{unspaced_var}}/example  # noqa: 206
```

## Plugins

Currently, there is a `salt-lint` plugin available for the following applications:

Application | GitHub Link | Store/Marketplace
:-:|:--|:--
Visual Studio Code | [warpnet/vscode-salt-lint](https://github.com/warpnet/vscode-salt-lint) | [VisualStudio Marketplace](https://marketplace.visualstudio.com/items?itemName=warpnet.salt-lint)
Sublime Text | [warpnet/SublimeLinter-salt-lint](https://github.com/warpnet/SublimeLinter-salt-lint) | [Package Control](https://packagecontrol.io/packages/SublimeLinter-contrib-salt-lint)
Vim ([ALE plugin](https://github.com/dense-analysis/ale)) | [dense-analysis/ale](https://github.com/dense-analysis/ale) | [GitHub](https://github.com/dense-analysis/ale)

Wish to create a `salt-lint` extension for your favourite editor? We're always looking for [contributions](CONTRIBUTING.md)!

## Fix common issues

`sed` might be one of the better tools to fix common issues, as shown in commands below.

**Note**: these commands assume your current working directory is the salt (states) directory/repository.

Fix spacing around `{{ var_name }}`, eg. `{{env}}` --> `{{ env }}`:\
`sed -i -E "s/\{\{\s?([^}]*[^} ])\s?\}\}/\{\{ \1 \}\}/g"  $(find . -name '*.sls')`

Make the `dir_mode`, `file_mode` and `mode` arguments in the desired syntax:\
`sed -i -E "s/\b(dir_|file_|)mode: 0?([0-7]{3})/\1mode: '0\2'/"  $(find . -name '*.sls')`

Add quotes around numeric values that start with a `0`:\
`sed -i -E "s/\b(minute|hour): (0[0-7]?)\$/\1: '\2'/"  $(find . -name '*.sls')`

## Acknowledgement

The project is heavily based on [ansible-lint](https://github.com/ansible/ansible-lint), with the modified work by [Warpnet B.V.](https://github.com/warpnet).  [ansible-lint](https://github.com/ansible/ansible-lint) was created by [Will Thames](https://github.com/willthames) and is now maintained as part of the [Ansible](https://www.ansible.com/) by [Red Hat](https://www.redhat.com) project.
