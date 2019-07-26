CameraRigLocalization
=====================

**Description**

This node retrieves the transformation between the tracked and the
optical reference frames.(?)
https://alicevision.github.io/#photogrammetry/localization

settings

====================== ======================================================================================================================================================================================
Name                   Description
====================== ======================================================================================================================================================================================
SfM Data               ``The sfmData file``
Media Path             The path to the video file, the folder of the image sequence or a text file (one image path per line) for each camera of the rig (eg. --mediapath /path/to/cam1.mov /path/to/cam2.mov)
Rig Calibration File   The file containing the calibration data for the rig (subposes)
Camera Intrinsics      The intrinsics calibration file for each camera of the rig. (eg. --cameraIntrinsics /path/to/calib1.txt /path/to/calib2.txt)
Descriptor Path        Folder containing the .desc
Match Describer Types  The describer types to use for the matching (sift', 'sift*float', 'sift*\ upright', 'akaze', 'akaze*liop', 'akaze*\ mldb', 'cctag3', 'cctag4', 'sift*ocv', 'akaze*\ ocv')
Preset                 Preset for the feature extractor when localizing a new image (low, medium, normal, high, ultra)
Resection Estimator    The type of /sac framework to use for resection (acransac, loransac)
Matching Estimator     The type of /sac framework to use for matching (acransac, loransac)
Refine Intrinsics      Enable/Disable camera intrinsics refinement for each localized image
Reprojection Error     Maximum reprojection error (in pixels) allowed for resectioning. If set to 0 it lets the ACRansac select an optimal value (0 - 10)
Use Localize Rig Naive Enable/Disable the naive method for rig localization: naive method tries to localize each camera separately
Angular Threshold      The maximum angular threshold in degrees between feature bearing vector and 3D point direction. Used only with the opengv method (0 - 10)
Voctree                [voctree] Filename for the vocabulary tree
Voctree Weights        [voctree] Filename for the vocabulary tree weights
Algorithm              [voctree] Algorithm type: {FirstBest, AllResults}
Nb Image Match         [voctree] Number of images to retrieve in the database
Max Results            [voctree] For algorithm AllResults, it stops the image matching when this number of matched images is reached. If 0 it is ignored (0 - 100)
Matching Error         [voctree] Maximum matching error (in pixels) allowed for image matching with geometric verification. If set to 0 it lets the ACRansac select an optimal value (0 - 10)
N Nearest Key Frames   [cctag] Number of images to retrieve in database (0 - 50)
Output Alembic         Filename for the SfMData export file (where camera poses will be stored) desc.Node.internalFolder + 'trackedcameras.abc
====================== ======================================================================================================================================================================================
