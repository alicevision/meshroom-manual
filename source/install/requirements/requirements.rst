Requirements
============

Hardware Requirements
~~~~~~~~~~~~~~~~~~~~~

.. warning::
  Meshroom requires an NVIDIA GPU card with a CUDA compute capability >= 2.0 for the MVS part. You can check your `CUDA Properties here <https://github.com/tpruvot/ccminer/wiki/Compatibility>`_ or on the `NVIDIA dev page <https://developer.nvidia.com/cuda-gpus>`_.

  In case you do not have a CUDA GPU, you can use the draft meshing option which uses the CPU for meshing.

Here are the minimum requirements for Meshroom:

+--------------------------------------------------------------------------+
| Minimum requirements                                                     |
+===================+======================================================+
| Operating systems | Windows x64, Linux, Mac OS X (some work required)    |
+-------------------+------------------------------------------------------+
| CPU               | Recent Intel or AMD cpus                             |
+-------------------+------------------------------------------------------+
| RAM Memory        | 8 GB                                                 |
+-------------------+------------------------------------------------------+
| Hard Drive        | ~400MB for Meshroom + space for your data            |
+-------------------+------------------------------------------------------+
| GPU               | NVIDIA CUDA-enabled GPU (compute capability >= 2.0)  |
+-------------------+------------------------------------------------------+

To obtain better performances on a desktop/laptop machine the recommended requirements are:

+--------------------------------------------------------------------------+
| Recommended requirements                                                 |
+===================+======================================================+
| CPU               | Intel Core i7 or AMD Ryzen 7                         |
+-------------------+------------------------------------------------------+
| RAM Memory        | 32 GB                                                |
+-------------------+------------------------------------------------------+
| Hard Drive        | 20GB+ HDD or SDD                                     |
+-------------------+------------------------------------------------------+
| GPU               | NVIDIA GeForce GTX 1070                              |
+-------------------+------------------------------------------------------+


Software Requirements
~~~~~~~~~~~~~~~~~~~~~

If you are using the pre-built binaries the only requirements is python.
Meshroom also relies on `AliceVision <https://github.com/alicevision/AliceVision>`_ framework.
AliceVision's binaries are shipped with the pre-built Meshroom package.

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


The pre-built binaries include the required python modules needed to run Meshroom.


AliceVision
+++++++++++

AliceVision library is included in the pre-built package.
If you want to build AliceVision yourself, follow this `guide <https://github.com/alicevision/AliceVision/blob/develop/INSTALL.md>`_.
