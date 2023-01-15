CameraCalibration
=================

**Description**

.. Note:: 
   At the moment this node can not directly be connected to the SfM pipeline in the UI. That would be obviously a nice feature to have.   
   The camera models and parameters can be manually copied to the CameraInit settings.
   This node just needs a bit more work before using it directly into the Meshroom graph. If someone is interested to contribute to this
   feature, we would be glad to provide assistance.



The internal camera parameters can be calibrated from multiple views of a checkerboard. This allows to retrieve focal length, principal point and distortion parameters. A detailed explanation is presented in [opencvCameraCalibration].

[opencvCameraCalibration] http://docs.opencv.org/3.0-beta/doc/tutorials/calib3d/camera_calibration/camera_calibration.html

========================= =============================================================================================================================
Name                      Description
========================= =============================================================================================================================
Input                     Input images in one of the following form: - folder containing images - image sequence like "/path/to/seq.@.jpg" - video file
Pattern                   Type of pattern (camera calibration patterns) - **CHESSBOARD** - CIRCLES - ASYMMETRIC CIRCLES - ASYMMETRIC CCTAG
Size                      (Size of the Pattern) - Number of inner corners per one of board dimension like Width (**7**) Height (**5**) (0-10000)
Square Size               Size of the grid's square cells (0-100mm) (**1**)
Nb Distortion Coef        Number of distortion coefficient (0-5) (**3**)
Max Frames                Maximal number of frames to extract from the video file (0-5) (**0**)
Max Calib Frames          Maximal number of frames to use to calibrate from the selected frames (0-1000)
Calib Grid Size           Define the number of cells per edge (0-50)
Min Input Frames          Minimal number of frames to limit the refinement loop (0-100)
Max Total Average Error   Max Total Average Error (0-1)
Debug Rejected Img Folder Folder to export delete images during the refinement loop
Debug Selected Img Folder Folder to export debug images
Output                    Output filename for intrinsic [and extrinsic] parameters (default filename cameraCalibration.cal)
========================= =============================================================================================================================

**Details**


**Sensor Calibration**

To calibrate a sensor a multistep process is required but can be completed from within Meshroom. Ensure that the camera settings, lens, and zoom settings remain consistent or the calibration will be different as these parameters chance. You may want to calibrate your camera setup if your sensor is not in the predefined database. To calibrate we will need a well lit flat surface or display and some somewhat accurate measuring tool or printer.

-   Generate a checkerboard calibration grid or use the grid from art toolkit github here: https://github.com/artoolkit/artoolkit5/blob/master/doc/patterns/Calibration%20chessboard%20%28A4%29.pdf
-   If using a display and measuring tool simply display the grid pattern full screen on your display. Measure the width of one of the grids in millimeters and keep this value handy.
-   If printing and using a flat surface ensure the page is not curling or distorted in any way as this will adversely affect calibration.
-   Record a video, or a set of still pictures with the checkerboard in many different angles and locations within the sensor. To get an idea of what this looks like there is an example video: https://vimeo.com/141414129.
-   Create a new node by right clicking within the empty space in the Graph Editor. Utils > CameraCalibration. Verify the following attributes:


Size of the pattern: This is the number of corners, in other words it is one less than the total number of squares counting both colors.

Size of the square in millimeters: If using the printed version 20mm squares is the default, verify size or measure directly.

Note the output folder or set your desired output path


- Open cameraCalibration.cal.txt from the output folder. The format of the file is:

// int #image width

// int #image height

// double #focal length

// double #ppx principal point x-coord

// double #ppy principal point y-coord

//DistortionParams:

// double #k0

// double #k1

// double #k2


-   Remove the CameraCalibration node as its outputs cannot be used in the Graph Editor at this time (v.2021.1).
-   Verify Advanced Attributes are checked. By clicking the 3 dots in the top right of the attributes panel.
-   Set CameraInit > Attributes > Intrinsics > InitalizationMode to Calibrated
-   Set CameraInit > Attributes > Intrinsics > Distortion Params to the K0,K1,K2 values.
-   Validate CameraInit > Attributes > Initial Focal Length
-   Validate CameraInit > Attributes > Focal Length
-   Validate CameraInit > Attributes > Sensor Width
-   Validate CameraInit > Attributes > Sensor Height
-   Validate CameraInit > Attributes > Principal Point

**Patterns**

CHESSBOARD https://github.com/artoolkit/artoolkit5/blob/master/doc/patterns/Calibration%20chessboard%20(A4).pdf 

Chessboard calibration video sample https://vimeo.com/141414129

CIRCLES

ASYMMETRIC_CIRCLES https://nerian.com/support/resources/patterns/

ASYMMETRIC_CCTAG https://github.com/alicevision/CCTag

A list with other camera calibration tools and patterns can be found here https://github.com/natowi/CameraCalibTools
