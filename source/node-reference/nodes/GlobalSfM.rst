GlobalSfM
=========

**Description**

GlobalSfM

MR version: 2020.x

settings

=============================================== ============================================================================================
Name                                            Description
=============================================== ============================================================================================
Input                                           SfM Data File
Features Folder
Features Folders                                Folder(s) containing the extracted features.
Matches Folder
Matches Folders                                 Folder(s) in which computed matches are stored.
Describer Types                                 Describer types used to describe an image.
                                                [**'sift'**, 'sift_float', 'sift_upright', 'akaze',
                                                'akaze_liop', 'akaze_mldb', 'cctag3', 'cctag4',
                                                'sift_ocv', 'akaze_ocv']
Rotation Averaging Method                       Method for rotation averaging :
                                
                                                * L1 minimization
                                
                                                * **L2 minimization**
Translation Averaging Method                    Method for translation averaging :
                                
                                                * L1 minimization\n"
                                
                                                * L2 minimization of sum of squared Chordal distances\n"
                                
                                                * **L1 soft minimization**
Force Lock of All Intrinsic Camera Parameters.  Force to keep constant all the intrinsics parameters of the cameras (focal length,
                                                principal point, distortion if any) during the reconstruction.
                                                This may be helpful if the input cameras are already fully calibrated.                               
Verbose Level                                   verbosity level (critical, error, warning, info, debug).
Output Folder                                   internalFolder
Output SfMData File                             Path to the output sfmdata file (internalFolder + 'SfmData.abc')
=============================================== ============================================================================================
