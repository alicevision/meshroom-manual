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
| Operating systems | Windows x64, Linux, macOS (some work required)       |
+-------------------+------------------------------------------------------+
| CPU               | Recent Intel or AMD cpus                             |
+-------------------+------------------------------------------------------+
| RAM Memory        | 8 GB                                                 |
+-------------------+------------------------------------------------------+
| Hard Drive        | ~400 MB for Meshroom + space for your data           |
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
| Hard Drive        | 20 GB+ HDD or SDD                                    |
+-------------------+------------------------------------------------------+
| GPU               | NVIDIA GeForce GTX 1070                              |
+-------------------+------------------------------------------------------+


Software Requirements
~~~~~~~~~~~~~~~~~~~~~

Meshroom is a Python application and it relies  on the `AliceVision <https://github.com/alicevision/AliceVision>`_ framework.
If you are using the pre-built binaries everything is shipped with the package, so you do not need to install anything else.

In case you are still planning to use the sources, see the paragraph *Software Requirements*
in the :ref:`building`_ section
