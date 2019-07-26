DepthMap
========

**Description**

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
