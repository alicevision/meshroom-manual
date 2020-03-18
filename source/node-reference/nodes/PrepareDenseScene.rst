PrepareDenseScene
=================

**Description**

-  This node undistorts the images and generates EXR images

   settings

========================= ========================================================================================
Name                      Description
========================= ========================================================================================
Input                     SfMData file
ImagesFolders             Use images from specific folder(s). Filename should be the same or the image uid.
Output File Type          Output file type for the undistorted images. (jpg, png, tif, **exr**)
Save Metadata             Save projections and intrinsics information in images metadata (only for .exr images).
Save Matrices Text Files  Save projections and intrinsics information in text files.
Correct images exposure   Apply a correction on images Exposure Value
Verbose Level             ['fatal', 'error', 'warning', 'info', 'debug', 'trace']
Output                    MVS Configuration file (desc.Node.internalFolder + 'mvs.ini)
Undistorted images        List of undistorted images.
========================= ========================================================================================

|image0|

.. |image0| image:: prepare-dense-scene.jpg
   :target: prepare-dense-scene.jpg

**ImagesFolders**

ImagesFolders option allows to override input images. This enables to use images with light patterns projected for SfM and MVS parts and do the Texturing with another set of images.
