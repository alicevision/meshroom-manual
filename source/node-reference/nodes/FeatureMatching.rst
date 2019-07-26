FeatureMatching
===============

**Description**

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

|image0|

.. |image0| image:: feature-matching.jpg
   :target: feature-matching.jpg
