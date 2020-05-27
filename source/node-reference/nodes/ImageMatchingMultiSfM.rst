ImageMatchingMultiSfM
=====================

**Description**

This node can combine image matching between two input SfMData.

Used for :ref:`live-reconstruction` and :ref:`augment-reconstruction`.

Settings

======================== ===========================================================================================================================================
Name                     Description
======================== ===========================================================================================================================================
Input A                  SfMData file
Input B                  SfMData file
Features Folders         Folder(s) containing the extracted features and descriptors
Tree                     Input name for the vocabulary tree file ALICEVISION_VOCTREE
Weights                  Input name for the weight file if not provided the weights will be computed on the database built with the provided set
Matching Mode            The mode to combine image matching between the input SfMData A and B: a/a+a/b for A with A + A with B. a/ab ['a/a+a/b' // 'a/ab' // 'a/b']
Minimal Number of Images Minimal number of images to use the vocabulary tree. If we have less features than this threshold we will compute all matching combinations
Max Descriptors          Limit the number of descriptors you load per image. Zero means no limit 500 (0-100000)
Nb Matches               The number of matches to retrieve for each image (If 0 it will retrieve all the matches) 50 (0-1000)
Verbose Level            verbosity level (fatal, error, warning, info, debug, trace)
Output List File         Filepath to the output file with the list of selected image pairs
Output Combined SfM      Path for the combined SfMData file internalFolder + 'combineSfM.sfm
======================== ===========================================================================================================================================

|image0|

.. |image0| image:: image-matching-multi.jpg
   :target: image-matching-multi.jpg
