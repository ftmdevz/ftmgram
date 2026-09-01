# FTMGram - Telegram MTProto API Client Library for Python
# Copyright (C) 2024-2026 FTM DEVELOPERZ <https://github.com/ftmdevz/ftmgram>

import os
import sys
import subprocess

sys.path.insert(0, os.path.abspath(".."))

from ftmgram import __version__
from ftmgram.raw.all import layer

project = "FTMGram"
copyright = "2024-2026, FTM DEVELOPERZ"
author = "FTM DEVELOPERZ"
version = "3.5.1"
release = "3.5.1"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None)
}

master_doc = "index"
source_suffix = ".rst"
autodoc_member_order = "bysource"

templates_path = ["_templates"]
html_copy_source = False

napoleon_use_rtype = False
napoleon_use_param = False

pygments_style = "sphinx"
highlight_language = "python3"
copybutton_prompt_text = "$ "
suppress_warnings = ["image.not_readable"]

html_title = "FTMGram"
html_theme = "furo"
html_static_path = [os.path.abspath("docs/static") if os.path.exists("docs/static") else os.path.abspath("static")]

html_css_files = [
    "css/all.min.css",
    "css/custom.css",
]
html_show_sourcelink = False
html_show_copyright = False
html_logo = "static/img/ftmgram_icon.svg"
html_favicon = "static/img/ftmgram_icon.svg"

html_theme_options = {
    "navigation_with_keys": True,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/ftmdevz/ftmgram",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
        {
            "name": "Telegram",
            "url": "https://t.me/ftmdeveloperz",
            "class": "fa-brands fa-solid fa-telegram fa-2x",
        },
    ],
    "dark_css_variables": {
        "color-brand-primary": "#f97316",
        "color-brand-content": "#fb923c",
        "color-sidebar-background": "#0d1117",
        "color-sidebar-background-border": "#30363d",
        "color-background-primary": "#0d1117",
        "color-background-secondary": "#161b22",
        "color-background-border": "#30363d",
    },
    "light_css_variables": {
        "color-brand-primary": "#ea580c",
        "color-brand-content": "#c2410c",
    },
}
