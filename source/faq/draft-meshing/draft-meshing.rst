Draft Meshing
=============

As of version 2019.1.0 of meshroom, it is possible to do a reconstruction without using the Depthmap node (depthmap requires CUDA). It is much faster than depth map but the resulting mesh is low quality, so it is still recommended that the depthmap is used to generate the mesh if possible. This can be done using the following node configuration: 

.. image:: draft-meshing.jpg

You should use the HIGH preset on the FeatureExtraction node to get enough density for the Meshing. `Reconstruction-parameters`_

.. _Reconstruction-parameters: https://github.com/alicevision/meshroom/wiki/Reconstruction-parameters