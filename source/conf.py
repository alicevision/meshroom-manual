# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import sphinx

#after doing the `pip install sphinx_rtd_theme`with the Sphinx's version of Python
import sphinx_rtd_theme

# The master toctree document.
master_doc = 'index'

project = 'Meshroom'
copyright = '2021. This work is licensed under a CC-BY-SA 4.0 International license.'
author = 'Meshroom Contributors'

# The full version, including alpha/beta/rc tags
version = 'v2021.1'
release = 'v2021.1.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosectionlabel', 'sphinx_rtd_theme', 'sphinxcontrib.bibtex']
sphinxVersion = sphinx.version_info
if(sphinxVersion[0] <= 1 and sphinxVersion[1] <= 8) :
	extensions.append('sphinx.ext.pngmath')
else:
	extensions.append('sphinx.ext.imgmath')


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes. sphinx_rtd_theme - search broken, table not soft break
#
#html_theme = 'default'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']
html_static_path = []

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "mr_logo.png"

# Latex/PDF generation Config
# Based on hints from:
# - https://stackoverflow.com/questions/54147210/how-to-add-copyright-notice-to-sphinx-generated-latex-documentation
# - https://www.sphinx-doc.org/en/master/latex.html
# - https://stackoverflow.com/questions/9745854/sphinx-pdf-themes
# - https://digitalsuperpowers.com/blog/2019-02-16-publishing-ebook.html
# - https://github.com/sphinx-doc/sphinx/pull/5850

latex_contents = r'''
    \setupHeadFootForFrontMatter
    \formattoc
    \maketitle
    \signaturepage
    \revisionhistory
    \tableofcontents
    \clearpage
    \listoffigures
    \clearpage
    \listoftables
    \clearpage
    \setupHeadFootForText
    \pagenumbering{arabic}
    \pagestyle{plain}
'''


latex_elements = {
    'fontpkg': r'''
\usepackage{lmodern}
''',
    'preamble': r'''
\newcommand\sphinxbackoftitlepage{%
\vspace*{\fill}
\begin{center}
''' + u"\u00A9 " + copyright + r''' \\
Revision: ''' + release + r''' \\
\url{https://alicevision.org}
\end{center}
\vspace*{\fill}
}
'''
}


latex_show_urls = 'footnote'
