FeatureExtraction
=================

**Description**

This step extracts features from the images, as well as descriptors for those features. It will change the file extension based on what type of feature you are extracting.

======================== ===========================================================================================================================================================================
Name                     Description
======================== ===========================================================================================================================================================================
**Input**                SfMData file.
**Describer Types**      Describer types used to describe an image. **'sift'**, 'sift*float', 'sift*\ upright', 'akaze', 'akaze*liop', 'akaze*\ mldb', 'cctag3', 'cctag4', 'sift*ocv', 'akaze*\ ocv'
**Describer Preset**     Control the ImageDescriber configuration (low, medium, **normal**, high, ultra). Configuration "ultra" can take long time !
**Force CPU Extraction** Use only CPU feature extraction.
**Max Nb Threads**       Specifies the maximum number of threads to run simultaneously (0 for automatic mode). (0-24) **0**
**Verbose Level**        verbosity level (fatal, error, warning, info, debug, trace).
**Output Folder**        Output path for the features and descriptors files (*.feat, \*.desc).
======================== ===========================================================================================================================================================================

**Force CPU Extraction**

Experimental feature. When disabled, GPU will be used. Speeds up
computation. Requires CUDA CC3+.


**Detailed description**

The objective of this step is to extract distinctive groups of pixels that are, to some extent, invariant to changing camera viewpoints during image acquisition. Hence, a feature in the scene should have similar feature descriptions in all images.

The most well-know feature detection method is the SIFT (Scale-invariant feature transform) algorithm. The initial goal of SIFT is to extract discriminative patches in a first image that can be compared to discriminative patches of a second image irrespective of rotation, translation, and scale. As a relevant detail only exists at a certain scale, the extracted patches are centered at stable points of interest. The key idea is that, to some extent, one can use the SIFT invariance to deal with the image transformations occurring when the viewpoints are changing during image acquisition.

From the representation of one image at different scales, which is technically done by computing a pyramid of downscaled images. SIFT computes scale-space maxima of the Laplacian representation, which is a specific image energy-based representation of the image, using so-called differences of Gaussians. These maxima correspond to points of interest. It then samples for each one of these maxima a square image patch whose origin is the maximum and x-direction is the dominant gradient at the origin. For each keypoint, a description of these patches is associated.

The description, which is typically stored in 128 bits, consists of a statistics of gradients computed in regions around the keypoint. The region size is determined by the keypoint scale and the orientation is determined by the dominant axis.

As the number of extracted features may vary a lot due to the variability of textures complexity (from one image to another or in different parts of the image), a post-filtering step is used to control the number of extracted features to reasonable limits (for instance between one and ten thousands per image). We use a grid filtering to ensure a good repartition in the image.

================== ==================================================================================================================================================================================================================================================================================
[Lowe2004]         `Distinctive image features from scale-invariant keypoints, David G. Lowe, 2004 <http://www.cs.ubc.ca/~lowe/papers/ijcv04.pdf>`__
[Otero2014]        `Anatomy of the SIFT Method, Ives Rey Otero, Mauricio Delbracio, 2014 <http://www.ipol.im/pub/art/2014/82/>`__
[Yu2011]           `ASIFT: An Algorithm for Fully Affine Invariant Comparison, Guoshen Yu, Jean-Michel Morel, 2011 <http://www.ipol.im/pub/art/2011/my-asift/>`__
[Alcantarilla2013] `AKAZE Fast explicit diffusion for accelerated features in nonlinear scale spaces, P.F. Alcantarilla, J. Nuevo, A. Bartoli, 2013 <http://www.bmva.org/bmvc/2013/Papers/paper0013/paper0013.pdf>`__
[Li2015]           `A survey of recent advances in visual feature detection, Yali Li, Shengjin Wang, Qi Tian, Xiaoqing Ding, 2015 <https://www.researchgate.net/profile/Yali_Li3/publication/273841042_A_survey_of_recent_advances_in_visual_feature_detection/links/5707d38408ae2eb9421bda3e.pdf>`__
[VLFEAT2008]       `VLFeat: An Open and Portable Library of Computer Vision Algorithms A. Vedaldi and B. Fulkerson, 2008 <http://www.vlfeat.org/>`__ `VLFeat SIFT detailed presentation <http://www.vlfeat.org/overview/sift.html>`__
================== ==================================================================================================================================================================================================================================================================================
