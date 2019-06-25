Error: This program needs a CUDA Enabled GPU
============================================

[error] This program needs a CUDA-Enabled GPU (with at least compute
capability 2.0), but Meshroom *is* running on a computer with an NVIDIA
GPU.

Solution: update/reinstall your drivers Details: `#182`_ `#197`_ `#203`_

This Error message on a computer *without* NVIDIA GPU
-----------------------------------------------------

The depth map computation is implemented with CUDA and requires an
NVIDIA GPU.

`#218`_ `#260`_

[Request] Remove CUDA dependency `alicevision/#439`_

   Currently, we have neither the interest nor the resources to do
   another implementation of the CUDA code to another GPU framework. If
   someone is willing to make this contribution, we will support and
   help for integration.\ `\*`_

Can I use Meshroom without an NVIDIA GPU?
-----------------------------------------

Yes, but you must use `Draft Meshing`_ to complete the reconstruction.

Does my GPU support CUDA?
-------------------------

Check `https://developer.nvidia.com/cuda-gpus`_

.. _#182: https://github.com/alicevision/meshroom/issues/182
.. _#197: https://github.com/alicevision/meshroom/issues/197
.. _#203: https://github.com/alicevision/meshroom/issues/203
.. _#218: https://github.com/alicevision/meshroom/issues/218
.. _#260: https://github.com/alicevision/meshroom/issues/260
.. _alicevision/#439: https://github.com/alicevision/AliceVision/issues/439
.. _\*: https://github.com/alicevision/AliceVision/issues/439#issuecomment-403820801
.. _Draft Meshing: https://github.com/alicevision/meshroom/wiki/Draft-Meshing
.. _`https://developer.nvidia.com/cuda-gpus`: https://developer.nvidia.com/cuda-gpus