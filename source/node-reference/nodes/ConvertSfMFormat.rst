ConvertSfMFormat
================

**Description**

-  creates abc', 'sfm', 'json', 'ply', 'baf SfM File from SfMData file

settings

====================== =========================================================================================================================================================================================
Name                   Description
====================== =========================================================================================================================================================================================
Input                  ``SfMData file``
SfM File Format        SfM File Format \ (output file extension: abc', 'sfm', 'json', 'ply', 'baf)`\`
Describer Types        Describer types to keep.\ ``'sift', 'sift_float', 'sift_upright', 'akaze', 'akaze_liop', 'akaze_mldb', 'cctag3', 'cctag4', 'sift_ocv', 'akaze_ocv'``
Image id               Image id
Image White List       image white list (uids or image paths).
Views                  Export views
Intrinsics             Export intrinsics
Extrinsics             Export extrinsics
Structure              Export structure
Observations           Export observations
Verbose Level          verbosity level (fatal, error, warning, info, debug, trace)
Output                 Path to the output SfM Data file. (desc.Node.internalFolder + 'sfm.{fileExtension})
Refine Intrinsics      Enable/Disable camera intrinsics refinement for each localized image
Reprojection Error     Maximum reprojection error (in pixels) allowed for resectioning. If set to 0 it lets the ACRansac select an optimal value (0 - 10)
Use Localize Rig Naive Enable/Disable the naive method for rig localization: naive method tries to localize each camera separately
Angular Threshold      The maximum angular threshold in degrees between feature bearing vector and 3D point direction. Used only with the opengv method (0 - 10)
Voctree                [voctree] Filename for the vocabulary tree
Voctree Weights        [voctree] Filename for the vocabulary tree weights
Algorithm              [voctree] Algorithm type: \ {FirstBest, AllResults}`\`
Nb Image Match         [voctree] Number of images to retrieve in the database
Max Results            [voctree] For algorithm AllResults, it stops the image matching when this number of matched images is reached. If 0 it is ignored (0 - 100)
Matching Error         [voctree] Maximum matching error (in pixels) allowed for image matching with geometric verification. If set to 0 it lets the ACRansac select an optimal value (0 - 10)
N Nearest Key Frames   [cctag] Number of images to retrieve in database (0 - 50)
Output Alembic         Filename for the SfMData export file (where camera poses will be stored) desc.Node.internalFolder + 'trackedcameras.abc
====================== =========================================================================================================================================================================================

**Input nodes:
StructureFromMotion:output\ :math:`\Rightarrow` \ input:ConvertSfMFormat**

|image0|

**Can I convert between Openmvg and alicevision SfM formats?**

OpenMVG and AliceVision json formats are very similar in the structure
but not compatible right away as openmvg is a data serialization file
among other things.
https://github.com/alicevision/AliceVision/issues/600

.. |image0| image:: convert-sfm-format.jpg
   :target: convert-sfm-format.jpg
