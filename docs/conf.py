import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "FTMGram"
copyright = "2024-2026, FTM DEVELOPERZ"
author = "FTM DEVELOPERZ"
release = "3.0.0"
version = "3.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "shibuya"
html_static_path = ["_static"]

html_theme_options = {
    "logo_target": "/",
    "github_url": "https://github.com/ftmdevz/ftmgram",
    "nav_links": [
        {"title": "Quick Start", "url": "quickstart"},
        {"title": "Install", "url": "installing"},
        {"title": "Changelog", "url": "changelog"},
    ],
    "accent_color": "orange",
}

html_logo = "_static/logo.png"
html_favicon = "_static/logo.png"
html_title = "FTMGram"

autodoc_member_order = "bysource"
autodoc_typehints = "description"
napoleon_google_docstring = True
napoleon_numpy_docstring = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
