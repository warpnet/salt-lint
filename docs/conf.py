import os
import sys
from datetime import datetime

sys.path.append("../")
sys.path.append(os.path.dirname(__file__))
import saltlint


project = saltlint.NAME
copyright = '{}, {}'.format(
    datetime.now().year,
    saltlint.__author__
)
author = saltlint.__author__
version = saltlint.__version__
release = version

extensions = ['m2r2']
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
source_suffix = ['.rst', '.md']

html_theme = 'alabaster'
html_theme_options = {
    "description": saltlint.DESCRIPTION,
    "show_powered_by": False,
    "github_user": "warpnet",
    "github_repo": "salt-lint",
    "github_button": True,
    "github_banner": True,
    "show_related": False,
}
html_static_path = ['_static']
