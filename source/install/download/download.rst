Getting Meshroom
================

Pre-built binaries
~~~~~~~~~~~~~~~~~~

Meshroom binaries can be downloaded from `https://alicevision.github.io/#meshroom <https://alicevision.github.io/#meshroom>`_

Prebuilt binaries on this page are all-in-one packages including AliceVision and all required resources.

.. note::
 The `pre-build version of Meshroom <https://github.com/alicevision/meshroom/releases>`_ may not include all the features of the developer version. Please check the `release notes <https://github.com/alicevision/meshroom/releases>`_ for further information.


From the sources
~~~~~~~~~~~~~~~~

If you want to run the latest version of Meshroom you need to get the sources.

Get the project
+++++++++++++++

See `INSTALL.md <https://github.com/alicevision/meshroom/blob/develop/INSTALL.md>`_ to setup the project and prerequisites.

Get the source code and install runtime requirements:

.. code::

  git clone --recursive git://github.com/alicevision/meshroom
  cd meshroom
  pip install -r requirements.txt


Set up requirements
+++++++++++++++++++

The ``requirements.txt`` file includes the required modules.
You can install them running:

.. code-block:: bash

  pip install -r requirements.txt -r dev_requirements.txt

.. note:: ``dev_requirements`` is only related to testing and packaging.
   It is not mandatory to run Meshroom.

In order to run Meshroom, some environment variables must be set for Meshroom to find the binaries and some other necessary files:

* Your ``PATH`` should contain the folder where the AliveVision binaries can be found.
  Suppose ``ALICEVISION_INSTALL`` contains the directory where the library is installed, then

 .. code-block:: bash

   PATH=$PATH:${ALICEVISION_INSTALL}/bin

* sensor database: a text database of sensor width per camera model which can be found in AliceVision installation

  .. code-block:: bash

    ALICEVISION_SENSOR_DB=${ALICEVISION_INSTALL}/share/aliceVision/cameraSensors.db


* [optional] vocabulary tree file: for larger datasets (>200 images), the vocabulary tree based matching greatly improves image matching performances.
  It can be downloaded from `here <https://gitlab.com/alicevision/trainedVocabularyTreeData/raw/master/vlfeat_K80L3.SIFT.tree>`_).
  
  .. code-block:: bash

    ALICEVISION_VOCTREE=/path/to/vlfeat_K80L3.SIFT.tree


Please refer to the section with the specific instructions for your OS for further details.
