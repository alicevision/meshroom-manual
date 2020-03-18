CameraInit
==========

**Description**

CameraInit loads image metadata, sensor information and generates viewpoints.sfm and cameraInit.sfm. You can mix multiple cameras and focal lengths.
The CameraInit will create groups of intrinsics based on the images metadata.
It is still good to have multiple images with the same camera and same focal lengths as it adds constraints on the internal cameras parameters. But you can combine multiple groups of images, it will not decrease the quality of the final model.

.. Note::
   In some cases, some image(s) have no serial number to identify the camera/lens device. This makes it impossible to correctly group the images by device if you have used multiple identical (same model) camera devices. The reconstruction will assume that only one device has been used, so if two images share the same focal length approximation they will share the same internal camera parameters. If you want to use multiple cameras, add a corresponding serialnumber to the EXIF data.

=========================== ========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
Viewpoints Input            viewpoints (1 Element for each loaded image) - ID - Pose ID - Image Path - Intrinsic: Internal Camera Parameters (Intrinsic ID) - Rig (-1 - 200) - Rig Sub-Pose: Rig Sub-Pose Parameters (-1 - 200) - Image Metadata: (list of metadata elements)
Intrinsic Camera Intrinsics - (1 Element for each loaded image) - ID - Initial Focal Length: Initial Guess on the Focal Length - Focal Length: Known/Calibrated Focal Length - Camera Type: pinhole', 'radial1', 'radial3', 'brown', 'fisheye4' - #Make: Camera Make (not included in this build, commented out) - #Model: Camera Model - #Sensor Width: Camera Sensor Width - Width: Image - Width (0-10000) - Height: Image Height (0-10000) - Serial Number: Device Serial Number (camera and lens combined) - Principal Point: X (0-10000) Y(0-10000)- DistortionParams: Distortion Parameters - Locked(True/False): If the camera has been calibrated, the internal camera parameters (intrinsics) can be locked. It should improve robustness and speedup the reconstruction. 
Sensor Database             Camera sensor width database path
Default Field Of View       Empirical value for the field of view in degree 45° (0°-180°)
Verbose Level               verbosity level (fatal, error, warning, info, debug, trace)
Output SfMData File         .../cameraInit.sfm
=========================== ========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

Details

The UID is based on the metadata. If there is no metadata it falls back to images file paths.

.. note::

   Issue: structure from motion reconstruction appears distorted, and has
   failed to aligned some groups of cameras when loading images without
   focal length

   Solution: Keep the " Focal Length" init value but set the "Initial Focal
   Length" to -1 if you are not sure of the value.

   https://github.com/alicevision/meshroom/issues/434
   
   
   .. Default Field Of View: is this horizontal, vertical, or diagonal FOV?
