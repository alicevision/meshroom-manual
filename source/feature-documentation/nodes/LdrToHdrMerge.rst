LdrToHdrMerge
=============

**Description**

Calibrate LDR to HDR response curve from samples

settings

================================ =================================================================================================
Name                             Description
================================ =================================================================================================
Input                            SfM Data File
Response file                    Response file
Number of Brackets               Number of exposure brackets per HDR image (0 for automatic detection).
Automatic Nb Brackets            Number of exposure brackets used per HDR image. It is detected automatically from input Viewpoints metadata if "userNbBrackets" is 0, else it is equal to "userNbBrackets".
Offset Ref Bracket Index         Zero to use the center bracket. +N to use a more exposed bracket or -N to use a less exposed backet.
Bypass                           Bypass HDR creation and use the medium bracket as the source for the next steps
Fusion Weight                    Weight function used to fuse all LDR images together
Channel Quantization Power       Quantization level like 8 bits or 10 bits.
Highlights Correction            Pixels saturated in all input images have a partial information about their real luminance.
                                 We only know that the value should be >= to the standard hdr fusion.
                                 This parameter allows to perform a post-processing step to put saturated pixels to a constant
                                 value defined by the `highlightsMaxLuminance` parameter.
                                 This parameter is float to enable to weight this correction.
Highlight Target Luminance (Lux) This is an arbitrary target value (in Lux) used to replace the unknown luminance value of the saturated pixels.
Storage Data Type                Storage image data type
Verbose Level                    ['fatal', 'error', 'warning', 'info', 'debug', 'trace']
Output SfMData File              Path to the output sfmdata file
================================ =================================================================================================

