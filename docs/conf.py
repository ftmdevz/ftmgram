import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "FTMGram"
copyright = "2024-2026, FTM DEVELOPERZ"
author = "FTM DEVELOPERZ"
release = "3.3.0"
version = "3.3.0"
version = "3.3.0"

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

autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}
napoleon_google_docstring = True
napoleon_numpy_docstring = False

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

html_theme = "shibuya"
html_static_path = ["_static"]
html_logo = "_static/logo.png"
html_favicon = "_static/logo.png"
html_title = "FTMGram"

html_theme_options = {
    "logo_target": "/",
    "github_url": "https://github.com/ftmdevz/ftmgram",
    "accent_color": "orange",
    "nav_links": [
        {"title": "Guide", "url": "intro/index"},
        {"title": "API Reference", "url": "api/index"},
        {"title": "Topics", "url": "topics/index"},
        {"title": "Changelog", "url": "changelog"},
    ],
    "og_image_url": "https://raw.githubusercontent.com/ftmdevz/ftmgram/ftmdevz/logo.png",
}

html_context = {
    "telegram_channel": "https://t.me/ftmdeveloperz",
    "telegram_chat": "https://t.me/ftmdevz",
    "pypi_url": "https://pypi.org/project/ftmgram/",
}
