Turntable
=========

To use a turntable, you should:
- On the FeatureMatching node, set the "Minimal 2D Motion" to a value of 2 pixels to avoid matching feature points that are exactly at the same location between 2 images.
- Add an ImageMasking node to make a color keying of the background.
The Input from the ImageMasking connects to CameraInit. The output of the ImageMasking node can be connected to the FeatureExtraction Masking Input and to the PrepareDenseScene Masking Input (applies the undistort to the mask and combines it with the RGB into an RGBA image, so the dense geometry will be computed only on the selected pixels).
If your background is not a uniform color, you can experiment with the ImageSegmentation node to segment the background, but it will less reliable that a color keying.

More details on the ImageMasking node: https://github.com/alicevision/Meshroom/wiki/New-Features-in-Meshroom-2023.1#1-image-masking

You can put markers in the scene to automatically scale the scene to real world coordinates:
See https://github.com/alicevision/Meshroom/wiki/CCTAG-scaling
