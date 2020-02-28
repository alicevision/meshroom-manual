Meshing
=======

**Description**

Generate Mesh from SfM point cloud or DepthMap

|image0|

.. |image0| image:: meshing.jpg
   :target: meshing.jpg


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
