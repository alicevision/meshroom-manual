DepthMap node too slow
======================

You can speed up the Depth Map process. Here is what you need to do:

Augment the downscale factor to directly reduce the precision.

Reduce the number of T cameras (sgmMaxTCams, refineMaxTCams) will directly reduce the computation time linearly, so if you change from 10 to 5 you will get a 2x speedup. 

A minimum value of 3 is necessary, 4 already gives decent results in many cases if the density of your acquisition process regular enough. 

The default value is necessary in large scale environment where it is difficult to have 4 images that cover the same area.(`#228`_)

.. _#228: https://github.com/alicevision/meshroom/issues/228#issuecomment-418329506