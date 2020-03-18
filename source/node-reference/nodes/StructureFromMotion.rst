StructureFromMotion
===================

**Description**

The StructureFromMotion (Incremental SfM) will reconstruct 3D points from the input images.
For Global SfM use the GlobalSfM node.


============================================== ==========================================================================================================================================================================================================================================================
Input                                          SfMData file
Features Folder                                Folder(s) containing the extracted features and descriptors.
Matches Folders                                Folder(s) in which computed matches are stored.
Describer Types                                Describer types used to describe an image. '**sift**', 'sift*float', 'sift*\ upright', 'akaze', 'akaze*liop', 'akaze*\ mldb', 'cctag3', 'cctag4', \**'sift\ *ocv', 'akaze*\ ocv'
Localizer Estimator                            Estimator type used to localize cameras (**acransac**, ransac, lsmeds, loransac, maxconsensus).
Localizer Max Ransac Iterations                Maximum number of iterations allowed in ransac step. (1-20000) **4096**
Localizer Max Ransac Error                     Maximum error (in pixels) allowed for camera localization (resectioning). If set to 0, it will select a threshold according to the localizer estimator used (if ACRansac, it will analyze the input data to select the optimal value). (0.0-100-0) **0.0**
Lock Scene Previously Reconstructed            This option is useful for SfM augmentation. Lock previously reconstructed poses and intrinsics.
Local Bundle Adjustment                        It reduces the reconstruction time, especially for large datasets (500+ images) by avoiding computation of the Bundle Adjustment on areas that are not changing.
LocalBA Graph Distance                         Graph-distance limit to define the Active region in the Local Bundle Adjustment strategy. (2-10) **1**
Maximum Number of Matches                      Maximum number of matches per image pair (and per feature type). This can be useful to have a quick reconstruction overview. 0 means no limit. (0-50000) **1**
Minimum Number of Matches                      Minimum number of matches per image pair (and per feature type). This can be useful to have a meaningful reconstruction with accurate keypoints. 0 means no limit. (0-50000) **1**
Min Input Track Length                         Minimum track length in input of SfM (**2**-10) 
Min Observation For Triangulation              Minimum number of observations to triangulate a point. Set it to 3 (or more) reduces drastically the noise in the point cloud, but the number of final poses is a little bit reduced (from 1.5% to 11% on the tested datasets). (**2**-10)
Min Angle For Triangulation                    Minimum angle for triangulation. (0.1-10) **3.0**
Min Angle For Landmark                         Minimum angle for landmark. (0.1-10) **2.0**
Max Reprojection Error                         Maximum reprojection error. (0.1-10) **4.0**
Min Angle Initial Pair                         Minimum angle for the initial pair. (0.1-10) **5.0**
Max Angle Initial Pair                         Maximum angle for the initial pair. (0.1-60) **40.0**
Use Only Matches From Input Folder             Use only matches from the input matchesFolder parameter. Matches folders previously added to the SfMData file will be ignored.
Use Rig Constraint                             Enable/Disable rig constraint.
Force Lock of All Intrinsic Camera Parameters. Force to keep constant all the intrinsics parameters of the cameras (focal length, principal point, distortion if any) during the reconstruction. This may be helpful if the input cameras are already fully calibrated.
Filter Track Forks                             Enable/Disable the track forks removal. A track contains a fork when incoherent matches lead to multiple features in the same image for a single track.
Initial Pair A                                 Filename of the first image (without path).
Initial Pair B                                 Filename of the second image (without path).
Inter File Extension                           Extension of the intermediate file export. ('.abc', '.ply')
Verbose Level                                  Verbosity level (fatal, error, warning, info, debug, trace).
Output SfMData File                            Path to the output sfmdata file (sfm.abc)
Output SfMData File                            Path to the output sfmdata file with cameras (views and poses). (cameras.sfm)
Output Folder                                  Folder for intermediate reconstruction files and additional reconstruction information files.
============================================== ==========================================================================================================================================================================================================================================================


|image0|

.. _header-n7:

.. |image0| image:: sfm.jpg
   :target: sfm.jpg

**Use Rig Constraint**
Add support for rig of cameras. This information is used as a new constraint in the SfM. 
This option can now be combined with localBA.
You need to use a specific folder hierarchy in the input images files (for instance: “/my/dataset/rig/0/DSLR_0001.JPG”, “/my/dataset/rig/1/DSLR_0001.JPG”) to provide this information.


**Detailed description**

The objective of this step is to understand the geometric relationship behind all the observations provided by the input images, and infer the rigid scene structure (3D points) with the pose (position and orientation) and internal calibration of all cameras. The Incremental pipeline is a growing reconstruction process. It first computes an initial two-view reconstruction that is iteratively extended by adding new views. 

First, it fuses all feature matches between image pairs into tracks. Each track is supposed to represent a point in space, visible from multiple cameras. However, at this step of the pipeline, it still contains many outliers. During this fusion of matches, we remove incoherent tracks.

Then, the incremental algorithm has to choose the best initial image pair. This choice is critical for the quality of the final reconstruction. It should indeed provide robust matches and contain reliable geometric information. So, this image pair should maximize the number of matches and the repartition of the corresponding features in each image. But at the same time, the angle between the cameras should also be large enough to provide reliable geometric information.

Then we compute the fundamental matrix between these 2 images and consider that the first one is the origin of the coordinate system. Now that we know the pose of the 2 first cameras, we can triangulate the corresponding 2D features into 3D points.

After that, we select all the images that have enough associations with the features that are already reconstructed in 3D. This algorithm is called next best views selection. Based on these 2D-3D associations it performs the resectioning of each of these new cameras. The resectioning is a Perspective-n-Point algorithm (PnP) in a RANSAC framework to find the pose of the camera that validates most of the features associations. On each camera, a non-linear minimization is performed to refine the pose.

From these new cameras poses, some tracks become visible by 2 or more resected cameras and it triangulates them. Then, we launch a Bundle Adjustment to refine everything: extrinsics and intrinsics parameters of all cameras as well as the position of all 3D points. We filter the results of the Bundle Adjustment by removing all observations that have high reprojection error or insufficient angles between observations.

As we have triangulated new points, we get more image candidates for next best views selection. We iterate like that, adding cameras and triangulating new 2D features into 3D points and removing 3D points that became invalidated, until we can’t localize new views.

Many other approaches exists like Global [Moulon2013], Hierarchical
[Havlena2010], [Toldo2015] or multi-stage [Shah2014] approaches.

**References**

============== =========================================================================================================================================================================
[Cheng2014]    Fast and Accurate Image Matching with Cascade Hashing for 3D Reconstruction Jian Cheng, Cong Leng, Jiaxiang Wu, Hainan Cui, Hanqing Lu. CVPR 2014
[Fischler1981] Random sample consensus: a paradigm for model fitting with applications to image analysis and automated cartography. Fischler, Martin A., and Robert C. Bolles. 1981
[Moulon2013]   Global Fusion of Relative Motions for Robust, Accurate and Scalable Structure from Motion. Pierre Moulon, Pascal Monasse and Renaud Marlet. ICCV 2013
[Moulon2012]   Adaptive structure from motion with a contrario model estimation. Pierre Moulon, Pascal Monasse, and Renaud Marlet. ACCV 2012
[Moulon2012]   Automatic homographic registration of a pair of images, with a contrario elimination of outliers. Moisan, Lionel, Pierre Moulon, and Pascal Monasse. IPOL 2012
[Moulon2012]   Unordered feature tracking made fast and easy, Pierre Moulon and Pascal Monasse, CVMP 2012
[Kneip2011]    A Novel Parametrization of the P3P-Problem for a Direct Computation of Absolute Camera Position and Orientation. Kneip, L.; Scaramuzza, D. ; Siegwart, R. CVPR 2011
[Lepetit2009]  EPnP: An Accurate O(n) Solution to the PnP Problem. V. Lepetit and F. Moreno-Noguer and P. Fua, IJCV 2009
[Nister2004]   An Efficient Solution to the Five-Point Relative Pose. D. Nister PAMI 2004
[Havlena2010]  Efficient Structure from Motion by Graph Optimization. M. Havlena, A. Torii, and T. Pajdla. ECCV 2010
[Toldo2015]    Hierarchical structure-and-motion recovery from uncalibrated images. R. Toldo, R. Gherardi, M. Farenzena and A. Fusiello. CVIU 2015
[Shah2014]     Multistage SFM: Revisiting Incremental Structure from Motion, Rajvi Shah, Aditya Deshpande, P J Narayanan, 2014
[Moulon2015]   `Robust and precise positioning of image networks, Pierre Moulon 2015 (in French) <https://hal.archives-ouvertes.fr/file/index/docid/996935/filename/These_MOULON.pdf>`__
[Martinec2008] Robust Multiview Reconstruction. Daniel Martinec, 2008
[Hartley2000]  Multiple view geometry in computer vision. Richard Hartley and Andrew Zisserman. Cambridge, 2000
[Ceres]        `Ceres Solver, Sameer Agarwal and Keir Mierle and Others <http://ceres-solver.org/>`__
[OpenGV]       `The OpenGV library <https://github.com/laurentkneip/opengv>`__
============== =========================================================================================================================================================================
