Supported image formats
=======================

Meshroom supports most image formats, including many RAW formats such as
'.exr', '.rw2', '.cr2', '.nef', '.arw',... The image importer is based
on `OpenImageIO`_, so all formats supported by OpenImageIO can be
imported to Meshroom. However it is recommended to use '.jpg', '.jpeg',
'.tif', '.tiff' or '.png' at the moment.

Note: On some datasets the reconstruction quality could be reduced or
cause unexpected interruption of the pipeline. (`#G`_) Convert your RAW
image to '.jpg', '.jpeg', '.tif', '.tiff' or '.png' to resolve this
problem.

.. _OpenImageIO: https://sites.google.com/site/openimageio/home
.. _#G: https://groups.google.com/forum/#!searchin/alicevision/raw|sort:date/alicevision/TzOcYo7tI9c/ihW70a9mCAAJ