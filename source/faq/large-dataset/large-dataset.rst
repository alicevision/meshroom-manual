Large scale dataset
===================

   Can I use Meshroom on large datasets with more than 1000 images?

Yes, the pipeline performance scales almost linearly. We recommend
adjusting the SfM parameters to be a bit more strict, as you know that
you have a good density / good connections between images. There are 2
global thresholds on the Meshing node (``maxInputPoints`` and
``maxPoints``) that may need to be adjusted depending on the
density/quality you need and the amount of RAM available on the computer
you use.

   Can I use Meshroom on renderfarm?

Meshroom has been designed to be used on renderfarm. It should be quite
straightforward to create a new submitter, see the `available
submitters`_ as examples. Contact us if you need more information to use
it with a new renderfarm system.

.. _available submitters: https://github.com/alicevision/meshroom/tree/develop/meshroom/submitters