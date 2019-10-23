Building Meshroom
====================

If you want to run the very latest version of Meshroom or some custom developer version, you need to get the sources.

Software Requirements
~~~~~~~~~~~~~~~~~~~~~

Meshroom is a Python application and it relies on the `AliceVision <https://github.com/alicevision/AliceVision>`_ framework.


Python Environment
++++++++++++++++++

The following versions of python are required:

* Windows: Python 3 (>=3.5)

* Linux / Mac OS X: Python 3 (>=3.5) or Python 2 (>= 2.7)

.. note::
  *No Python 2.7 support on Windows?*

  Official Python 2.7 binary package is built with Visual Studio 2008, while PySide2/Qt is built using Visual Studio 2015/2017.
  Therefore, in order to avoid mixing MSVC runtime libraries, Qt does not ship PySide2 wheels for Python 2.7 on Windows (as explained `here <https://wiki.qt.io/Qt_for_Python/Considerations#Missing_Windows_.2F_Python_2.7_release>`_).
  Note that for using Meshroom in command line mode only (no UI), PySide2 is not required and Python 2.7 would be fine.


Get the project
~~~~~~~~~~~~~~~

See `INSTALL.md <https://github.com/alicevision/meshroom/blob/develop/INSTALL.md>`_ to setup the project and prerequisites.

Get the source code and install runtime requirements:

.. code::

  git clone --recursive git://github.com/alicevision/meshroom
  cd meshroom
  pip install -r requirements.txt
