MeshDecimate
============

**Description**

Simplify your mesh to reduce mesh size without changing visual
appearance of the model.

settings

============================ ===================================================================================================================================================================
Name                         Description
============================ ===================================================================================================================================================================
Input Mesh (OBJ file format)
Simplification factor        Simplification factor 0.5 (0 - 1)
Fixed Number of Vertice      Fixed number of output vertices 0 (0 - 1 000 000)
Min Vertices                 Min number of output vertices 0 (0 - 1 000 000)
Max Vertices                 Max number of output vertices 0 (0 - 1 000 000)
Flip Normals                 Option to flip face normals 'It can be needed as it depends on the vertices order in triangles and the convention change from one software to another. (True/False)
Verbose Level                verbosity level (fatal // error // warning // info // debug // trace)
Output mesh                  Output mesh (OBJ file format) internalFolder + 'mesh.obj
============================ ===================================================================================================================================================================

|image0|

or Meshing\ :math:`\Rightarrow` \ MeshDecimate\ :math:`\Rightarrow` \ MeshFiltering?

**Comparison MeshDecimate and MeshResampling**

|image1|

**Flip Normals**

|image2|

.. |image0| image:: mesh-decimate.jpg
   :target: mesh-decimate.jpg
.. |image1| image:: compare-resampling-decimate.jpg
   :target: compare-resampling-decimate.jpg
.. |image2| image:: flip-normals.jpg
   :target: flip-normals.jpg
