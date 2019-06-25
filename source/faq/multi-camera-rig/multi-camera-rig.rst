Multi Camera Rig
================

If you shoot a static dataset with a moving rig of cameras (cameras
rigidly fixed together with shutter synchronization), you can declare
this constraint to the reconstruction algorithm.

Currently, there is no solution to declare this constraint directly
within the Meshroom UI, but you can use the following file naming
convention:

::

   + rig/  # "rig" folder
   |-+ 0/  # sub-folder with the index of the camera (starting at 0)
   |---- DSC_0001.JPG  # Your camera filename (the is no constraint on the filename, here "DSC_" prefix is just an example)
   |---- DSC_0002.JPG
   |-+ 1/ # sub-folder with the index of the camera
   |---- DSC_0001.JPG
   |---- DSC_0002.JPG

All images with the same name in different "rig/cameraIndex" folder will
be declared linked together by the same transformation. So in this
example, the relative pose between the 2 "DSC_0001.JPG" images from the
camera 0 and camera 1 will be the same than between the 2 "DSC_0002.JPG"
images.

When you drop your images into Meshroom, this constraint will be
recognized and you will be able to see it in the ``CameraInit`` node
(see ``Rig`` and ``Rig Sub-Pose`` of the ``Viewpoints`` parameter).