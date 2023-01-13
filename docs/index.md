<a href="https://github.com/warpnet/salt-lint" style="color: black;">
    <h1 align="center">salt-lint</h1>
</a>
<p align="center">
    <a href="https://pypi.org/project/salt-lint/">
        <img src="https://img.shields.io/github/v/release/warpnet/salt-lint?style=for-the-badge"
            alt="Latest release version">
    </a>
    <a href="https://pypi.org/project/salt-lint/">
        <img src="https://img.shields.io/pypi/pyversions/salt-lint?style=for-the-badge"
            alt="PyPI - Python Version">
    </a>
    <a href="https://raw.githubusercontent.com/warpnet/salt-lint/main/LICENSE">
        <img src="https://img.shields.io/pypi/l/salt-lint?style=for-the-badge&color=blue"
            alt="PyPI - License">
    </a>
    <a href="https://github.com/warpnet/salt-lint/actions">
        <img src="https://img.shields.io/github/workflow/status/warpnet/salt-lint/tests?style=for-the-badge&color=blue"
            alt="GitHub Workflow Status">
    </a>
    <a href="https://github.com/warpnet/salt-lint/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/warpnet/salt-lint?style=for-the-badge&color=blue"
            alt="GitHub contributors">
    </a>
    </br>
    <b>salt-lint</b> checks Salt State files (SLS) for best practices and behavior that could potentially be improved.
    <br />
    <a href="https://github.com/warpnet/salt-lint/"><strong>Explore the code »</strong></a>
    <br />
    <a href="https://salt-lint.readthedocs.io/en/latest/rules/">Check the Linting Rules</a>
    ·
    <a href="https://github.com/warpnet/salt-lint/issues/new?assignees=&labels=Type%3A%20Bug&template=bug_report.md&title=Bug%3A">Report Bug</a>
    ·
    <a href="https://github.com/warpnet/salt-lint/issues/new?assignees=&labels=Type%3A%20Enhancement&template=feature_request.md&title=Feature+Request%3A">Request Feature</a>
</p>

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
docker run -v $(pwd):/data:ro --entrypoint=/bin/bash -it warpnetbv/salt-lint:latest -c 'find /data -type f -name "*.sls" -print0 | xargs -0 --no-run-if-empty salt-lint'
```

On a system with SELinux, change `:ro` to `:Z`. Example below uses podman:

```bash
podman run -v $(pwd):/data:Z --entrypoint=/bin/bash -it warpnetbv/salt-lint:latest -c 'find /data -type f -name "*.sls" -print0 | xargs -0 --no-run-if-empty salt-lint'
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

To use salt-lint with [pre-commit](https://pre-commit.com), just add the following to your local repo's `.pre-commit-config.yaml` file. Prior to version 0.12.0 of [pre-commit](https://pre-commit.com) the file was `hooks.yaml` (now `.pre-commit-config.yaml`).

```yaml
---
repos:
  - repo: https://github.com/warpnet/salt-lint
    rev: v0.9.0
    hooks:
      - id: salt-lint
```

Optionally override the default file selection as follows:

```yaml
      ...
      - id: salt-lint
        files: \.(sls|jinja|tmpl)$
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
