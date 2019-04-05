Salt-lint
=========

``salt-lint`` checks Salt state files (SLS) for practices and behaviour that could
potentially be improved.

The project is heavily based on `ansible-lint`_, which was created by `Will Thames`_ and is now maintained as part of the `Ansible`_ by `Red Hat`_ project.

Installing
==========

From Source
-----------

.. code-block:: bash

    pip install git+https://github.com/roaldnefs/salt-lint.git

Usage
=====

Command Line Options
--------------------

The following is the output from ``salt-lint --help``, providing an overview of the basic command line options:

.. code-block:: bash

    Usage: salt-lint [options] init.sls [state ...]

    Options:
      --version             show program's version number and exit
      -h, --help            show this help message and exit
      -L                    list all the rules
      -t TAGS               only check rules whose id/tags match these values
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

Linting Salt state files
------------------------

It's important to note tat ``salt-lint`` accepts a list of Salt state files or a list of directories.

Configuring
===========

Configuration File
------------------

Salt-lint supports local confguration via a ``.salt-lint`` configuration file. Salt-lint check the working directory for the presence of this file and applies any configuration found there. The configuration file location can also be overridden via the ``-c path/to/file`` CLI flag.

If a value is provided on both the command line and via a config file, the values will be merged (if a list like **exclude_paths**), or the **True** value will be preferred, in the case of something like **quiet**.

Pre-commit Setup
----------------

To use salt-lint with `pre-commit`_,  just add the following to your local repo's ``.pre-commit-config.yaml`` file. Prior to version 0.12.0 of `pre-commit`_ the file was ``hooks.yaml`` (now ``.pre-commit-config.yaml``).

.. code-block:: yaml

    ---

    # For use with pre-commit.
    # See usage instructions at http://pre-commit.com

    -   id: salt-lint
        name: Salt-lint
        description: This hook runs salt-lint.
        entry: salt-lint
        language: python
        files: \.(sls)$


Authors
=======

salt-lint is heavily based on `ansible-lint`_ with the modified work by `Roald Nefs`_. `ansible-lint`_ was created by `Will Thames`_ and is now maintained as part of the `Ansible`_ by `Red Hat`_ project.

.. _pre-commit: https://pre-commit.com
.. _ansible-lint: https://github.com/ansible/ansible-lint 
.. _Roald Nefs: https://github.com/roaldnefs
.. _Will Thames: https://github.com/willthames
.. _Ansible: https://ansible.com
.. _Red Hat: https://redhat.com
