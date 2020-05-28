DepthMap
========

.. note::
   This node requires CUDA

**Description**

Retrieves the depth value of each pixel for all cameras that have been resolved by SfM.

--------------

settings

============================== =================================================================================================================
Name                           Description
============================== =================================================================================================================
``MVS Configuration File:``    SfMData file.
Images Folder                  Use images from a specific folder instead of those specify in the SfMData file. Filename should be the image uid.
Downscale                      Image downscale factor (1, 2, 4, 8, 16)
Min View Angle                 Minimum angle between two views.(0.0 - 10.0)
Max View Angle                 Maximum angle between two views. (10.0 - 120.0)
SGM: Nb Neighbour Cameras      Semi Global Matching: Number of neighbour cameras (1 - 100)
SGM: WSH: Semi Global Matching Half-size of the patch used to compute the similarity (1 - 20)
SGM: GammaC                    Semi Global Matching: GammaC Threshold (0 - 30)
SGM: GammaP                    Semi Global Matching: GammaP Threshold (0 - 30)
Refine: Number of samples      (1 - 500)
Refine: Number of Depths       (1 - 100)
Refine: Number of Iterations   (1 - 500)
Refine: Nb Neighbour Cameras   Refine: Number of neighbour cameras. (1 - 20)
Refine: WSH                    Refine: Half-size of the patch used to compute the similarity. (1 - 20)
Refine: Sigma                  Refine: Sigma Threshold (0 - 30)
Refine: GammaC                 Refine: GammaC Threshold. (0 - 30)
Refine: GammaP                 Refine: GammaP threshold. (0 - 30)
Refine: Tc or Rc pixel size    Use minimum pixel size of neighbour cameras (Tc) or current camera pixel size (Rc)
Verbose Level                  verbosity level (fatal, error, warning, info, debug, trace)
Output                         Output folder for generated depth maps
============================== =================================================================================================================

**default:**

|image0|

.. |image0| image:: depth-map.jpg
   :target: depth-map.jpg

**Detailed description**

For all cameras that have been resolved by SfM, we want to retrieve the depth value of each pixel. Many approaches exist, like Block Matching, Semi-Global Matching (SGM) :cite:`Hirschmüller2005`, :cite:`Hirschmüller2008` or ADCensus :cite:`Mei2011`. We will focus on the SGM method implemented in AliceVision.

For each image, we select the N best/closest cameras around. We select fronto-parallel planes based on the intersection of the optical axis with the pixels of the selected neighboring cameras. This creates a volume W, H, Z with many depth candidates per pixel. We estimate the similarity for all of them. The similarity is computed by the Zero Mean Normalized Cross-Correlation (ZNCC) of a small patch in the main image reprojected into the other camera. This create a volume of similarities. For each neighboring image, we accumulate similarities into this volume. This volume is very noisy. We apply a filtering step along X and Y axes which accumulates local costs which drastically reduce the score of isolated high values. We finally select the local minima and replace the selected plane index with the depth value stored into a depth map. This depth map has banding artifacts as it is based on the original selection of depth values. So a refine step is applied to get depth values with sub-pixel accuracy.

All these depth maps can be computed independently in parallel. Then we apply a filtering step to ensure consistency between multiple cameras. A compromise is chosen based on both similarity value and the number of coherent cameras to keep weakly supported surfaces without adding artefacts.

Additional references: :cite:`Strecha2006`, :cite:`Scharstein2002`

