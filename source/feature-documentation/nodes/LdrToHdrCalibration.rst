LdrToHdrCalibration
===================

**Description**

Calibrate LDR to HDR response curve from samples

settings

============================== =================================================================================================
Name                           Description
============================== =================================================================================================
Input                          SfM Data File
Samples folder                 Samples folder
Bypass                         Bypass HDR creation and use the medium bracket as the source for the next steps
Calibration Method             Method used for camera calibration
Calibration Weight             Weight function used to calibrate camera response
Number of Brackets             Number of exposure brackets per HDR image (0 for automatic detection).
Automatic Nb Brackets          Number of exposure brackets used per HDR image. It is detected automatically from input Viewpoints metadata if "userNbBrackets" is 0, else it is equal to "userNbBrackets".
Channel Quantization Power     Quantization level like 8 bits or 10 bits.
Max Number of Points           Max number of points used from the sampling. This ensures that the number of pixels values extracted by the sampling can be managed by the calibration step (in term of computation time and memory usage).
Verbose Level                  ['fatal', 'error', 'warning', 'info', 'debug', 'trace']
Output response  File          Path to the output response file
============================== =================================================================================================

