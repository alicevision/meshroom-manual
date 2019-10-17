[![CC BY-SA 4.0](https://img.shields.io/badge/license-CC%20BY--SA%204.0-blue.svg?style=flat-square)](https://creativecommons.org/licenses/by-sa/4.0/)
[![language: ReStructuredText](https://img.shields.io/badge/language-RST-black.svg?style=flat-square)](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
![HitCount](http://hits.dwyl.io/natowi/meshroom_doc.svg)
[![all releases](https://img.shields.io/github/downloads/natowi/meshroom_doc/total.svg?style=flat-square&color=success)](https://github.com/natowi/meshroom_doc/releases/)
![pre-release](https://img.shields.io/github/release-pre/natowi/meshroom_doc.svg?style=flat-square&color=yellow&label=pre-release)
![release](https://img.shields.io/github/release/natowi/meshroom_doc.svg?style=flat-square&color=green&label=release)
[![Travis](https://img.shields.io/travis/natowi/meshroom_doc.svg?style=flat-square)](https://travis-ci.org/natowi/meshroom_doc)

# About

**This is documentation is work in progress. Do not expect a polished document at this stage.**

See [Project ToDo](https://github.com/alicevision/meshroom-manual/projects) for details. Please do not fork at the moment, unless you would like to contribute.

I am new to ReStructuredText and open to suggestions.

# Next update
The next big update is planned for October 2019
+ capturing images for photogrammetry chapters
+ MR2019.2 updates
+ improved layout
+ new pdf release
+ preperation for readthedocs release

# How to contribute

-   make yourself familiar with ReStructuredText and Sphinx
-   do not make any changes to the general structure (yet)
-   open an Issue for questions

I could use some help with:
- optimizing the formatting for pdf&html
- anything listed here https://github.com/alicevision/meshroom-manual/projects

# How to build on windows

-   (install pip)
-   **pip install sphinx**
-   in your cli, navigate to the meshroom\_doc directory
-   type **make html** (this will re-/build the html doc)

For other build methods read the sphinx documentation

# FAQ

**Why Github?**

-   easier to manage
-   no spam
-   accessible

**Why Restructured Text?**

-   can be converted to various formats, including html and pdf using Sphinx

**How to edit and preview Restructured Text?**

-   You can use [Atom](https://atom.io/) with the [RestructuredText Preview Pandoc](https://atom.io/packages/rst-preview-pandoc) Plugin

**Release versions**

Format: v00.00.000

Example: v19.02.001 doc for Meshroom 2019.2, update 001
