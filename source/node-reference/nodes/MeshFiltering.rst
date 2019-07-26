MeshFiltering
=============

**Description**

Filter out unwanted elements of your mesh

settings

============================= ============================================================================================================================================================
Name                          Description
============================= ============================================================================================================================================================
Input                         Input Mesh (OBJ file format)
Filter Large Triangles Factor Remove all large triangles. We consider a triangle as large if one edge is bigger than N times the average edge length. Put zero to disable it. 60 (1 - 100)
Keep Only the Largest Mesh    Keep only the largest connected triangles group (True/False)
Nb Iterations                 5 (0 - 50)
Lambda                        1 (0-10
Verbose Level                
Verbose Level                 ['fatal', 'error', 'warning', 'info', 'debug', 'trace']
Output mesh                   Output mesh (OBJ file format) internalFolder + 'mesh.obj
============================= ============================================================================================================================================================

|image0|

.. Note::

   "Keep Only The Largest Mesh". This is disabled by default in the
   2019.1.0 release to avoid that the environment is being meshed, but not
   the object of interest. The largest Mesh is in some cases the
   reconstructed background. When the object of interest is not connected
   to the large background mesh it will be removed. You should place your
   object of interest on a well structured non transparent or reflecting
   surface (e.g. a newspaper).

.. |image0| image:: mesh-filtering.jpg
   :target: mesh-filtering.jpg
