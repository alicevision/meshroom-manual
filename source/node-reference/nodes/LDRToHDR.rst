LDRToHDR
========

**Description**

======================== =============================================================================================================================================================
Name                     Description
======================== =============================================================================================================================================================
Input                    List of LDR images or a folder containing them
Calibration Method       Method used for camera calibration. - **linear** - robertson - debevec - beta: grossberg
Input Response           external camera response file path to fuse all LDR images together.
Target Exposure Image    LDR image at the target exposure for the output HDR image to be centered.
Calibration Weight       Weight function type (default, gaussian, triangle, plateau). ['default', 'gaussian', 'triangle', 'plateau']
Fusion Weight            Weight function used to fuse all LDR images together (**gaussian**, triangle, plateau).
Oversaturated Correction Oversaturated correction for pixels oversaturated in all images: - use 0 for no correction - use 0.5 for interior lighting - use 1 for outdoor lighting (0-1)
Recover Path             Path to write recovered LDR image at the target exposure by applying inverse response on HDR image.
Verbose Level            Verbosity level (fatal, error, warning, **info**, debug, trace).
Output                   Output HDR image path. desc.Node.internalFolder + 'hdr.exr'
Output Response          Output response function path. desc.Node.internalFolder + 'response.ods'
======================== =============================================================================================================================================================

|image0|
|image1|

.. |image0| image:: ldr2hdr.JPG
   :target: ldr2hdr.JPG
   
.. |image1| image:: ldr2hdr-1.JPG
   :target: ldr2hdr-1.JPG