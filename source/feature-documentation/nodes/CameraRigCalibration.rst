CameraRigCalibration
====================

**Description**

If a rig of cameras is used, we can perform the rig calibration. We
localize cameras individually on the whole sequence. Then we use all
valid poses to compute the relative poses between cameras of the rig and
choose the more stable value across the images. Then we initialize the
rig relative pose with this value and perform a global Bundle Adjustment
on all the cameras of the rig. When the rig is calibrated, we can use it
to directly localize the rig pose from the synchronized multi-cameras
system with [Kneip2014] approaches.

..The rig calibration find the relative poses between all cameras used.
It takes a point cloud as input and can use both CCTag and SIFT features
for localization. The implication is that all cameras must see features
(either SIFT or CCTag) that are part of the point cloud, but they do not
have to observe overlapping regions. (See:POPART: Previz for Onset
Production Adaptive Realtime Tracking)

“Given the position of the tracked reference frame relative to the
motion capture system and the optical reference frames it is possible to
retrieve the transformation between the tracked and the optical
reference frames”1 “In practice, it is particularly difficult to make
the tracked frame coincident with the camera optical frame, thus a
calibration procedure is needed to estimate this transformation and
achieve the millimetric accuracy” [Chiodini et al. 2018]

[Chiodini et al. 2018] Chiodini, Sebastiano & Pertile, Marco &
Giubilato, Riccardo & Salvioli, Federico & Barrera, Marco &
Franceschetti, Paola & Debei, Stefano. (2018). Camera Rig Extrinsic
Calibration Using a Motion Capture System.
10.1109/MetroAeroSpace.2018.8453603.
https://www.researchgate.net/publication/327513182\ *Camera*\ Rig\ *Extrinsic*\ Calibration\ *Using*\ a\ *Motion*\ Capture_System

https://alicevision.github.io/#photogrammetry/localization


**References**

:cite:`Kneip2011`

[Kneip2013] Using Multi-Camera Systems in Robotics: Efficient Solutions
to the NPnP ProblemL. Kneip, P. Furgale, R. Siegwart. May 2013

[Kneip2014] OpenGV: A unified and generalized approach to real-time
calibrated geometric vision, L. Kneip, P. Furgale. May 2014.

[Kneip2014] Efficient Computation of Relative Pose for Multi-Camera
Systems. L. Kneip, H. Li. June 2014

**Settings**

===================== ======================================================================================================================================================================================
Name                  Description
===================== ======================================================================================================================================================================================
\                    
SfM Data              The sfmData file
Media Path            The path to the video file, the folder of the image sequence or a text file (one image path per line) for each camera of the rig (eg. --mediapath /path/to/cam1.mov /path/to/cam2.mov)
Camera Intrinsics     The intrinsics calibration file for each camera of the rig. (eg. --cameraIntrinsics /path/to/calib1.txt /path/to/calib2.txt)
Export                Filename for the alembic file containing the rig poses with the 3D points. It also saves a file for each camera named 'filename.cam##.abc (trackedcameras.abc)
Descriptor Path       Folder containing the .desc
Match Describer Types The describer types to use for the matching 'sift', 'sift*float', 'sift*\ upright', 'akaze', 'akaze*liop', 'akaze*\ mldb', 'cctag3', 'cctag4', 'sift*ocv', 'akaze*\ ocv'
Preset                Preset for the feature extractor when localizing a new image (low, medium, normal, high, ultra)
Resection Estimator   The type of /sac framework to use for resection (acransac
Matching Estimator    The type of /sac framework to use for matching (acransac, loransac)
Refine Intrinsics     Enable/Disable camera intrinsics refinement for each localized image
Reprojection Error    Maximum reprojection error (in pixels) allowed for resectioning. If set to 0 it lets the ACRansac select an optimal value. (0 - 10)
Max Input Frames      Maximum number of frames to read in input. 0 means no limit (0 - 1000)
Voctree               [voctree] Filename for the vocabulary tree
Voctree Weights       [voctree] Filename for the vocabulary tree weights
Algorithm             [voctree] Algorithm type: {FirstBest, AllResults}
Nb Image Match        [voctree] Number of images to retrieve in the database (0 - 50)
Max Results           [voctree] For algorithm AllResults, it stops the image matching when this number of matched images is reached. If 0 it is ignored (0 - 100)
Matching Error        [voctree] Maximum matching error (in pixels) allowed for image matching with geometric verification. If set to 0 it lets the ACRansac select an optimal value (0 - 10)
N Nearest Key Frames  [cctag] Number of images to retrieve in database (0 - 50)
Output File           The name of the file where to store the calibration data (desc.Node.internalFolder + 'cameraRigCalibration.rigCal)
===================== ======================================================================================================================================================================================


**Voctree Weights**: http://www.ipol.im/pub/art/2018/199/ voctree
(optional): For larger datasets (/>200 images), greatly improves image
matching performances. It can be downloaded here.
https://github.com/fragofer/voctree You need to specify the path to
vlfeat_K80L3.SIFT.tree in **Voctree**.


