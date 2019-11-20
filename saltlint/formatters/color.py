# -*- coding: utf-8 -*-

# Modified version of color.py from saltstack. Saltstack licensed as follows:
#
#
#   Salt - Remote execution system
#
#   Copyright 2014-2019 SaltStack Team
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#


'''
Functions used for CLI color themes.
'''

# Import Python libs
from __future__ import absolute_import, print_function, unicode_literals

# Import Salt libs
import six
from .textformat import TextFormat


def get_colors(use=True):
    '''
    Return the colors as an easy to use dict. Pass `False` to deactivate all
    colors by setting them to empty strings. Pass a string containing only the
    name of a single color to be used in place of all colors. Examples:

    .. code-block:: python

        colors = get_colors()  # enable all colors
        no_colors = get_colors(False)  # disable all colors
        red_colors = get_colors('RED')  # set all colors to red

    '''

    colors = {
        'BLACK': TextFormat('black'),
        'DARK_GRAY': TextFormat('bold', 'black'),
        'RED': TextFormat('red'),
        'LIGHT_RED': TextFormat('bold', 'red'),
        'GREEN': TextFormat('green'),
        'LIGHT_GREEN': TextFormat('bold', 'green'),
        'YELLOW': TextFormat('yellow'),
        'LIGHT_YELLOW': TextFormat('bold', 'yellow'),
        'BLUE': TextFormat('blue'),
        'LIGHT_BLUE': TextFormat('bold', 'blue'),
        'MAGENTA': TextFormat('magenta'),
        'LIGHT_MAGENTA': TextFormat('bold', 'magenta'),
        'CYAN': TextFormat('cyan'),
        'LIGHT_CYAN': TextFormat('bold', 'cyan'),
        'LIGHT_GRAY': TextFormat('white'),
        'WHITE': TextFormat('bold', 'white'),
        'DEFAULT_COLOR': TextFormat('default'),
        'ENDC': TextFormat('reset'),
    }

    if not use:
        for color in colors:
            colors[color] = ''
    if isinstance(use, six.string_types):
        # Try to set all of the colors to the passed color
        if use in colors:
            for color in colors:
                # except for color reset
                if color == 'ENDC':
                    continue
                colors[color] = colors[use]

    return colors
