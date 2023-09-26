Docker
======

An official docker image of Meshroom can be found on `Docker Hub <https://hub.docker.com/r/alicevision/meshroom>`_.
The relevant Dockerfile can be found in the `root directory of the sources <https://github.com/alicevision/meshroom/blob/master/Dockerfile>`_

The image is based on the NVIDIA docker which needs to be installed.
You can follow the official NVIDIA tutorial `here <https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)>`_.

To execute the docker image:

.. code-block:: bash

  docker pull alicevision/meshroom
  docker run -it --runtime=nvidia meshroom
