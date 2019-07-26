Troubleshooting
===============

Things you can check/try:

-  make sure the downloaded Meshroom files are not corrupted
   (incomplete/interrupted download)

-  avoid special characters/non-ASCII characters in Meshroom and images
   file paths (`#209`_)

-  make sure your antivirus program does not interfere with Meshroom
   ((`#178`_)/(\ `#342`_))

-  are you running Meshroom as Admin? (This will disable drag-and-drop
   on windows)

-  Check your Python installation /reinstall as admin and check the PATH
   if there are any conflicts

-  update/install latest NVIDIA drivers

-  set your NVIDIA GPU as primary GPU for Meshroom. (NVIDIA Control
   Panel :math:`\Rightarrow` Manage 3D Settings)

-  Try the Meshroom 2018.1 release; when using windows 7 try the
   corresponding release (Meshroom 2019.1 has some problems with
   Texturing `#449`_, DepthMap and some photo datasets which worked in
   2018.1 `#409`_. These problems will be addressed in the next release)

-  Test Meshroom with the `Monstree`_ dataset

-  Sometimes the pipeline is corrupted. Clear the cache for the node
   (and following nodes) with the error. Sometimes restarting the
   application / the computer might help. #201

-  `check your images`_ for problems

.. _#209: https://github.com/alicevision/meshroom/issues/209
.. _#178: https://github.com/alicevision/meshroom/issues/178
.. _#342: https://github.com/alicevision/meshroom/issues/342
.. _#449: https://github.com/alicevision/meshroom/issues/449
.. _#409: https://github.com/alicevision/meshroom/issues/409
.. _Monstree: https://github.com/alicevision/dataset_monstree
.. _check your images: Images-cannot-be-imported