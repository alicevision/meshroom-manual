ExportMatches
=============

**Description** 

Saves features and descriptors files (.feat, .desc) to folder


settings

======================= =================================================================================================
Name                    Description
======================= =================================================================================================
Input                   SfMData file
Describer Types         Describer types used to describe an image. 
                        [**'sift'**, 'sift_float', 'sift_upright', 'akaze', 'akaze_liop', 'akaze_mldb', 'cctag3',
                        'cctag4', 'sift_ocv', 'akaze_ocv'],
Features Folder         
Features Folders        Folder(s) containing the extracted features and descriptors.
Matches Folder          
Matches Folders         Folder(s) in which computed matches are stored.

Verbose Level           ['fatal', 'error', 'warning', 'info', 'debug', 'trace']
Output                  Output path for the features and descriptors files (.feat, .desc). (internalFolder)
======================= =================================================================================================
