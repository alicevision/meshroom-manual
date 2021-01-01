ExportAnimatedCamera
====================

**Description**

ExportAnimatedCamera creates an Alembic animatedCamera.abc file from SFMData (e.g. for use in 3D Compositing software)

The Animated Camera export feature is not optimized at the moment and requires a sequence of images with corresponding names (1-n) from the same folder. Unstructured images, naming conventions, folder structures... will not work or result in an error.

settings

========================= ======================================================================================
Name                      Description
========================= ======================================================================================
Input SfMData             SfMData file containing a complete SfM
SfMData Filter            A SfMData file use as filter
Export Undistorted Images Export Undistorted Images value=True
Undistort Image Format    Image file format to use for undistorted images (\*.jpg, \*.jpg, \*.tif, \*.exr (half))
Verbose Level             verbosity level (fatal, error, warning, info, debug, trace)
Output filepath           Output filepath for the alembic animated camera
Output Camera Filepath    Output filename for the alembic animated camera internalFolder + 'camera.abc'
========================= ======================================================================================

SFM to ExportAnimatedCamera Details:
https://www.youtube.com/watch?v=1dhdEmGLZhY
