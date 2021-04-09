Supported Formats
=================

Image File formats
------------------

**Supported file extensions of Images / Image Viewer:**

All image formats supported by the `OIIO library <https://github.com/OpenImageIO/oiio>`_ such as:

'.jpg', '.jpeg', '.tif', '.tiff', '.png', '.exr', '.rw2', '.cr2', '.nef', '.arw'.

can be imported to Meshroom. However there might be some unexpected behaviour when using RAW images.


Video File formats
------------------

.avi', '.mov', '.qt', '.mkv', '.webm', '.mp4', '.mpg', '.mpeg', '.m2v', '.m4v', '.wmv', '.ogv', '.ogg', '.mxf'

Panoramas
---------

panoramaInfoExtensions: '.xml'

3D File formats
---------------

.. csv-table::
   :header: "Name", "Refernce", "Description"
   :widths: 15, 10, 30

   "Alembic (.abc)", "`Alembic <http://www.alembic.io/>`_ ", "cloud_and_poses Alembic is a format for storing information about animated scenes after programmatic elements have been applied."
   "OBJ", "", "OBJ is a very strict ASCII format for encoding vertices, points, faces and textures first introduced by Wavefront Technologies."
   "PLY", "`PLY <https://people.sc.fsu.edu/~jburkardt/data/ply/ply.html>`_ ", "The Polygon File Format (or Stanford Triangle Format) has an ASCII representation and a binary representation. It is inspired by the OBJ format that allows the definition of arbitrary properties for every point. This allows an implementation to add arbitrary information to points including accuracy information, but not in any backward-compatible way. Camera information could be included in comments."
   "SfM", "", ""

FBX support (paused) https://github.com/alicevision/AliceVision/pull/174

Alembic is the preferred choice for intermediate storage of points clouds, because it is the only format that is already supported by all of the major 3d software packages.

Other file formats
------------------

**.bin** denseReconstruction: The bin format is only useful to get the visibility information of each vertex (no color information)

**.cal** calibration file

**.desc** describer file

**.EXR** OpenEXR image format: for depth map images

**.txt** text file list to describer image parameters
**.ini** A configuration file

**.json** describes the used image dataset

**.baf (sfm)** Bundle Adjustment File Export SfM data (Intrinsics/Poses/Landmarks)
