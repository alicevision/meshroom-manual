Meshing
=======

**Description**

Generate Mesh from SfM point cloud or DepthMap

=================================================== ==============================================================================================================================================================================================================================================
Name                                                Description
=================================================== ==============================================================================================================================================================================================================================================
Input                                               SfMData file.
Depth Maps Folder                                   Input depth maps folder
Filtered Depth Maps Folder                          Input filtered depth maps folder
Estimate Space From SfM                             Estimate the 3d space from the SfM
Min Observations For SfM Space Estimation           Minimum number of observations for SfM space estimation. (0-100) **3**
Min Observations Angle For SfM Space Estimation     Minimum angle between two observations for SfM space estimation. (0-120) **10**
Max Input Points                                    Max input points loaded from depth map images (500**000** - 500\ **000**\ 000) 
Max Points                                          Max points at the end of the depth maps fusion (100**000** - 10\ **000**\ 000) 
Max Points Per Voxel                                (500**000** – 30\ **000**\ 000) 
Min Step                                            The step used to load depth values from depth maps is computed from maxInputPts. Here we define the minimal value for this step, so on small datasets we will not spend too much time at the beginning loading all depth values (1- 20) **2** 
Partitioning                                        (**singleBlock**, auto) 
Repartition                                         (**multiResolution**, regularGrid) 
angleFactor                                         (0.0-200.0) **15.0**
simFactor                                           (0.0-200.0) **1.0**
pixSizeMarginInitCoef                               (0.0-10.0) **2.0**
pixSizeMarginFinalCoef                              (0.0-10.0) **4.0**
voteMarginFactor                                    (0.1-10.0) **4.0**
contributeMarginFactor                              (0.0-10.0) **2.0**
simGaussianSizeInit                                 (0.0-50) **10.0**
simGaussianSize                                     (0.0-50) **0.1**
minAngleThreshold                                   (0.0-10.0) **0.01**
Refine Fuse                                         Refine depth map fusion with the new pixels size defined by angle and similarity scores.
Add Landmarks To The Dense Point Cloud              Add SfM Landmarks to the dense point cloud.
Colorize Output                                     Whether to colorize output dense point cloud and mesh.
Save Raw Dense Point Cloud                          Save dense point cloud before cut and filtering.
Verbose Level                                       verbosity level (fatal, error, warning, **info**, debug, trace).
Output Mesh                                         Output mesh (OBJ file format). mesh.obj
Output Dense Point Cloud                            Output dense point cloud with visibilities (SfMData file format). densePointCloud.abc
=================================================== ==============================================================================================================================================================================================================================================

**Detailed description**

The objective of this step is to create a dense geometric surface representation of the scene.

First, we fuse all the depth maps into a global octree where compatible depth values are merged into the octree cells.

We then perform a 3D Delaunay tetrahedralization. Then a complex voting procedure is done to compute weights on cells and weights on facets connecting the cells as explained in [Jancosek2011] and [Jancosek2014].

A Graph Cut Max-Flow [Boykov2004] is applied to optimally cut the volume. This cut represents the extracted mesh surface. We filter bad cells on the surface. We finally apply a Laplacian filtering on the mesh to remove local artefacts.

At this point, the mesh can also be simplified to reduce unnecessary vertices.

============== ===============================================================================================================================================
[Jancosek2014] Exploiting Visibility Information in Surface Reconstruction to Preserve Weakly Supported Surfaces, Michal Jancosek, Tomas Pajdla
[Jancosek2011] Multi-view reconstruction preserving weakly-supported surfaces, Michal Jancosek, Tomas Pajdla, CVPR 2011
[Jancosek2010] Hallucination-free multi-view stereo, M. Jancosek and T. Pajdla, ECCV 2010
[Labatut2009]  Robust and efficient surface reconstruction from range data, P. Labatut, J.-P. Pons, and R. Keriven, 2009
[Boykov2004]   An Experimental Comparison of Min-Cut/Max-Flow Algorithms for Energy Minimization in Computer Vision, Yuri Boykov and Vladimir Kolmogorov. 2004
============== ===============================================================================================================================================
