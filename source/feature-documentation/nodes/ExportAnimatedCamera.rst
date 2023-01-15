ExportAnimatedCamera
====================

**Description**

ExportAnimatedCamera creates an Alembic animatedCamera.abc file from SFMData (e.g. for use in 3D Compositing software)

The Animated Camera export feature is not optimized at the moment and requires a sequence of images with corresponding names (1-n) located in a single folder. Unstructured images, naming conventions, and other folder structures will not work properly.

The UV maps exported by Meshroom can be used to remove lens distortion of input images in other compositing applications.

settings

========================= ======================================================================================
Name                      Description
========================= ======================================================================================
Input SfMData             SfMData file containing a complete SfM
SfMData Filter            A SfMData file use as filter
Export UV Maps            Exports a lens un-distortion UV map as an .exr file
Export Undistorted Images Exports images without lens distortion
Undistort Image Format    Image file format to use for undistorted images (\*.jpg, \*.jpg, \*.tif, \*.exr (half))
Export Full ROD
Correct Principal Point   Moves the center of exported UV maps and undistorted images to the calculated lens optical center when true
Verbose Level             Verbosity level (fatal, error, warning, info, debug, trace)
Output filepath           Output filepath for the alembic animated camera
Output Camera Filepath    Output filename for the alembic animated camera internalFolder + 'camera.abc'
========================= ======================================================================================

SFM to ExportAnimatedCamera Details:
https://www.youtube.com/watch?v=1dhdEmGLZhY
