FeatureMatching
===============

**Description**

Finds the correspondence between the images, using feature descriptors.

settings

=========================== ==========================================================================================================================================================================================================================================================================================================================================================================================================================
Name                        Description
=========================== ==========================================================================================================================================================================================================================================================================================================================================================================================================================
Input                       SfMData file
Features Folder            
Features Folders            Folder(s) containing the extracted features and descriptors
Image Pairs List            Path to a file which contains the list of image pairs to match
Describer Types             Describer types used to describe an image ``**sift**'/ 'sift_float'/ 'sift_upright'/ 'akaze'/ 'akaze_liop'/ 'akaze_mldb'/ 'cctag3'/ 'cctag4'/ 'sift_ocv'/ 'akaze_ocv``
Photometric Matching Method ``For Scalar based regions descriptor ' * BRUTE_FORCE_L2: L2  BruteForce matching' ' * ANN_L2: L2 Approximate Nearest Neighbor  matching ' * CASCADE_HASHING_L2: L2 Cascade Hashing matching ' *  FAST_CASCADE_HASHING_L2: L2 Cascade Hashing with precomputed hashed  regions (faster than CASCADE_HASHING_L2 but use more memory) 'For Binary  based descriptor  ' * BRUTE_FORCE_HAMMING: BruteForce Hamming matching'``
Geometric Estimator         Geometric estimator: ``(acransac:  A-Contrario Ransac //  loransac: LO-Ransac (only available for fundamental_matrix model)``
Geometric Filter Type       Geometric validation method to filter features matches: ``**fundamental_matrix** // essential_matrix // homography_matrix /// homography_growing // no_filtering'``
Distance Ratio              ``Distance ratio to discard non meaningful matches 0.8 (0.0 - 1)``
Max Iteration               Maximum number of iterations allowed in ransac step 2048 ``(1 - 20000)``
Max Matches                 Maximum number of matches to keep ``(0 - 10000)``
Save Putative Matches       putative matches (True/False)
Guided Matching             the found model to improve the pairwise correspondences (True/False)
Export Debug Files          debug files (svg/ dot) (True/False)
Verbose Level               verbosity level (fatal, error, warning, info, debug, trace)
Output Folder               Path to a folder in which computed matches will be stored
=========================== ==========================================================================================================================================================================================================================================================================================================================================================================================================================

**Detailed description**

The objective of this step is to match all features between candidate image pairs.

First, we perform photometric matches between the set of descriptors from the 2 input images. For each feature in image A, we obtain a list of candidate features in image B. As the descriptor space is not a linear and well defined space, we cannot rely on absolute distance values to know if the match is valid or not (we can only have an absolute higher bound distance). To remove bad candidates, we assume that there’s only one valid match in the other image. So for each feature descriptor on the first image, we look for the 2 closest descriptors and we use a relative threshold between them. This assumption will kill features on repetitive structure but has proved to be a robust criterion [Lowe2004]. This provide a list of feature matching candidates based only on a photometric criterion. Find the 2 closest descriptors in the second image for each feature is computationally intensive with a brute force approach, but many optimized algorithms exists. The most common one is Approximate Nearest Neighbor, but there are alternatives like, Cascading Hashing.

Then, we use the features positions in the images to make a geometric filtering by using epipolar geometry in an outlier detection framework called RANSAC (RANdom SAmple Consensus). We randomly select a small set of feature correspondences and compute the fundamental (or essential) matrix, then we check the number of features that validates this model and iterate through the RANSAC framework.

=========== =================================================================================================================================
[Lowe2004]  `Distinctive image features from scale-invariant keypoints, David G. Lowe, 2004 <http://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf>`__
[FLANN2009] Fast Approximate Nearest Neighbors with Automatic Algorithm Configuration. Muja, Marius, and David G. Lowe. VISAPP (1). 2009
=========== =================================================================================================================================

