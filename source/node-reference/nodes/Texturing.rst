Texturing
=========

**Description**

Texturing creates UVs and projects the textures change quality and size/
file type of texture

============================= =====================================================================================================================================================================================================================================================================
MVS Configuration file        .../mvs.ini
Input Dense Reconstruction    Path to the dense reconstruction result (mesh with per vertex visibility) 
Other Input Mesh              Optional input mesh to texture. By default, it will texture the result of the reconstruction.
Texture Side                  Output texture size 1024, 2048, 4096, **8192**, 16384
Texture Downscale             Texture downscale factor1, **2**, 4, 8
Texture File Type             Texture File Type 'jpg', **'png'**, 'tiff', 'exr' 
Unwrap Method                 Method to unwrap input mesh if it does not have UV coordinates **Basic** (> 600k faces) fast and simple. Can generate multiple atlases LSCM (<= 600k faces): optimize space. Generates one atlas ABF (<= 300k faces): optimize space and stretch. Generates one atlas
Fill Holes                    Fill Texture holes with plausible values True/\ **False**
Padding                       Texture edge padding size in pixel (0-100)
Max Nb of Images For Fusion   Max number of images to combine to create the final texture (0-10)
Best Score Threshold          0.0 to disable filtering based on threshold to relative best score (0.0-1.0)
Angle Hard Threshold          0.0 to disable angle hard threshold filtering (0.0, 180.0)
Force Visible By All Vertices Triangle visibility is based on the union of vertices visiblity.True/\ **False**
Flip Normals                  Option to flip face normals. It can be needed as it depends on the vertices order in triangles and the convention change from one software to another.
Visibility Remapping Method   Method to remap visibilities from the reconstruction to the input mesh (Pull, Push, **PullPush**).
Verbose Level                 verbosity level (fatal, error, warning, **info**, debug, trace).
Output Folder                 Folder for output mesh: OBJ, material and texture files.
Output Mesh                   Folder for output mesh: OBJ, material and texture files. internalFolder + 'texturedMesh.obj
Output Material               Folder for output mesh: OBJ, material and texture files. internalFolder + 'texturedMesh.mtl
Output Textures               Folder for output mesh: OBJ, material and texture files. internalFolder + 'texture_*.png 
============================= =====================================================================================================================================================================================================================================================================

**About:**

**Texture Downscale**

Downscaling to 4 or 8 will reduce the texture quality but speed up the
computation time.

Set Texture Downscale to 1 instead of 2 to get the maximum possible
resolution with the resolution of your images.

**Best Score Threshold**

This parameter is a contraint to limit the number of source images we
use in the color fusion. It is not related to the number of output
texture files. There is no such parameter, the only thing you can do is
to increase the image resolution.

**Unwrap Method**

If you decimate your mesh to a reasonable size, you can also change the
unwrapMethod to LSCM or ABF which will generate only one texture file.
But it will not work if you mesh is too heavy, check the tooltip:

Method to unwrap input mesh if it does not have UV coordinates.

-  Basic (> 600k faces) fast and simple. Can generate multiple atlases.

-  LSCM (<= 600k faces): optimize space. Generates one atlas.

-  ABF (<= 300k faces): optimize space and stretch. Generates one atlas.

   https://github.com/alicevision/meshroom/issues/211#issuecomment-416184229


|image0|

.. |image0| image:: texturing.jpg
   :target: texturing.jpg

The approach is based on a generalization of the multi-band blending in [Burt1983] applied to 3D texturing with weighting strategies based on visibility and varying resolution. It is in the same spirit than [Baumberg2002] and [Allene2008].

**References**

============== =========================================================================================================================================================================
[Burt1983]      `A Multiresolution Spline with Application to Image Mosaics. P. J. Burt and E. H. Adelson. ACM Trans. Graph. 1983 <https://doi.org/10.1145/245.247>`__
[Baumberg2002]  `Blending images for texturing 3D models. A. Baumberg. BMVC 2002 <http://www.bmva.org/bmvc/2002/papers/49/full_49.pdf>`__
[Allene2008]    `Seamless image-based texture atlases using multi-band blending. C. Allene and J. Pons and R. Keriven. ICPR 2008 <https://doi.org/10.1109/ICPR.2008.4761913>`__
============== =========================================================================================================================================================================