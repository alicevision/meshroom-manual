LdrToHdrSampling
============

**Description**

Sample pixels from Low range images for HDR creation

settings

============================== =================================================================================================
Name                           Description
============================== =================================================================================================
Input                          SfM Data File
Number of Brackets             Number of exposure brackets per HDR image (0 for automatic detection).
Automatic Nb Brackets          Number of exposure brackets used per HDR image. It is detected automatically from input Viewpoints metadata if "userNbBrackets" is 0, else it is equal to "userNbBrackets".
Bypass                         Bypass HDR creation and use the medium bracket as the source for the next steps
Channel Quantization Power     Quantization level like 8 bits or 10 bits.
Block Size                     Size of the image tile to extract a sample.
Patch Radius                   Radius of the patch used to analyze the sample statistics.
Max Number of Samples          Max number of samples per image group.
Export Debug Files             Export debug files to analyze the sampling strategy.
Verbose Level                  ['fatal', 'error', 'warning', 'info', 'debug', 'trace']
Output                         Output path for the samples.
============================== =================================================================================================

