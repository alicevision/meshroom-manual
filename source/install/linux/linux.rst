Linux
~~~~~

**Get the project**

See `INSTALL.md <https://github.com/alicevision/meshroom/blob/develop/INSTALL.md>`_ to setup the project and prerequisites.

Get the source code and install runtime requirements:

*git clone --recursive git://github.com/alicevision/meshroom*

*cd meshroom*

*pip install -r requirements.txt*

**Start Meshroom**

You need to have `AliceVision <https://github.com/alicevision/AliceVision>`_ installation in your
**PATH** and **LD_LIBRARY_PATH**.

**Launch the User Interface**

*# Linux/macOS*

*PYTHONPATH=$PWD python meshroom/ui*

**Note:**

On some distributions (e.g Ubuntu), you may have conflicts between native drivers and mesa drivers, resulting in an empty black window. In that case, you need to force usage of native drivers by adding them to the

*LD_LIBRARY_PATH:*

*LD_LIBRARY_PATH=/usr/lib/nvidia-340 ./Meshroom*

You may need to adjust the folder

*/usr/lib/nvidia-340*

with the correct driver version.

On Ubuntu, you may have conflicts between native drivers and mesa drivers. In that case, you need to force usage of native drivers by adding them to the

*LD_LIBRARY_PATH:*

*LD_LIBRARY_PATH=/usr/lib/nvidia-340 PYTHONPATH=$PWD python meshroom/ui*


You may need to adjust the folder **/usr/lib/nvidia-340** with the correct driver version.

Do not use foreign characters in path names (latin characters only).

**Launch a 3D reconstruction in command line**

**Linux:**
*PYTHONPATH=$PWD*

*python bin/meshroom_photogrammetry --input INPUT_IMAGES_FOLDER --output OUTPUT_FOLDER*

German:
http://paravel.org/blog/2018/12/10/how-to-photogrammetry-mit-meshroom-unter-ubuntu-16-04

.. source: https://github.com/alicevision/meshroom
.. source: https://github.com/alicevision/meshroom/releases
