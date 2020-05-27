[![CC BY-SA 4.0](https://img.shields.io/badge/license-CC%20BY--SA%204.0-blue.svg?style=flat-square)](https://creativecommons.org/licenses/by-sa/4.0/)
[![language: ReStructuredText](https://img.shields.io/badge/language-RST-black.svg?style=flat-square)](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
![HitCount](http://hits.dwyl.io/natowi/meshroom_doc.svg)
[![all releases](https://img.shields.io/github/downloads/natowi/meshroom_doc/total.svg?style=flat-square&color=success)](https://readthedocs.org/projects/meshroom-manual/downloads/)
![Read the Docs](https://img.shields.io/readthedocs/meshroom-manual.svg?style=flat-square&color=success)

# About

**This is documentation is work in progress.**

See [Project ToDo](https://github.com/alicevision/meshroom-manual/projects) for details.

# Next update
+ capturing images for photogrammetry chapters
+ MR2019.2 updates
+ improved layout
+ readthedocs release (including pdf) https://meshroom-manual.readthedocs.io

# How to contribute

-   make yourself familiar with ReStructuredText and Sphinx
-   do not make any changes to the general structure (yet)
-   open an Issue for questions

We could use some help with:
- optimizing the formatting for pdf&html
- anything listed here https://github.com/alicevision/meshroom-manual/projects

# How to Build

- install Python 3
- install a latex package
- install pip and the rtd theme
```bash 
pip install -r requirements.txt
```

-   in your cli, navigate to the `meshroom-manual` directory
-   type `make html` (this will re-/build the html doc)

For other build methods read the sphinx documentation.

# FAQ

**Why Restructured Text?**

-   can be converted to various formats, including html and pdf using Sphinx

**How to edit and preview Restructured Text?**

-   You can use [Atom](https://atom.io/) with the [RestructuredText Preview Pandoc](https://atom.io/packages/rst-preview-pandoc) Plugin
-   [Typora](https://www.typora.io) is a friendly editor
-   [Visual Studio Code](https://code.visualstudio.com) with the [reStructuredText](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext) extension 

**Release versions**

Format: v00.00.000

Example: v19.02.001 doc for Meshroom 2019.2, update 001
