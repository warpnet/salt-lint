# Copyright (c) 2013-2018 Will Thames <will@thames.id.au>
# Copyright (c) 2018 Ansible by Red Hat
# Modified work Copyright (c) 2019 Roald Nefs

from __future__ import absolute_import, division, print_function
__metaclass__ = type

try:
    import pkg_resources
except ImportError:
    pass


try:
    __version__ = pkg_resources.get_distribution('salt-lint').version
except Exception:
    __verion__ = 'unknown'
