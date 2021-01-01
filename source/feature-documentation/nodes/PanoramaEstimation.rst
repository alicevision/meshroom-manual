PanoramaEstimation
==================

**Description**


settings

=============================================== =================================================================================================
Name                                            Description
=============================================== =================================================================================================
Input                                           SfM Data File
Features Folder
Features Folders                                Folder(s) containing the extracted features.
Matches Folder
Matches Folders                                 Folder(s) in which computed matches are stored.
Describer Types                                 Describer types used to describe an image. [**'sift'**, 'sift_float', 'sift_upright', 'akaze',
                                                'akaze_liop', 'akaze_mldb', 'cctag3', 'cctag4', 'sift_ocv', 'akaze_ocv']
Orientation                                     Orientation (**0**-6)
Longitude offset (deg.)                         Offset to the panorama longitude (-180.0-180.0, **0**)
Latitude offset (deg.)                          Offset to the panorama latitude (-90.0-90.0, **0**)
Rotation Averaging Method                       Method for rotation averaging :

                                                * L1 minimization
                          
                                                * **L2 minimization**
Relative Rotation Method                        Method for relative rotation :

                                                * from essential matrix
                        
                                                * from **homography matrix**
Refine                                          Refine camera relative poses, points and optionally internal camera parameter
Force Lock of All Intrinsic Camera Parameters.  Force to keep constant all the intrinsics parameters of the cameras (focal length,
                                                principal point, distortion if any) during the reconstruction.
                                                This may be helpful if the input cameras are already fully calibrated.
                                                
Verbose Level                                   ['fatal', 'error', 'warning', 'info', 'debug', 'trace']
Output Folder                                   internalFolder
Output SfMData File                             Path to the output sfmdata file (internalFolder + 'sfmData.abc)
=============================================== =================================================================================================
