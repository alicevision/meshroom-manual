HDR Panorama Pipeline
=====================

* fusion of multi-bracketing LDR images into HDR
* alignment of panorama images
* support for fisheye optics
* automatically estimate fisheye circle or manually edit it
* take advantage of motorized-head file

Nodes
+++++

#. :doc:`/feature-documentation/nodes/CameraInit`
#. :doc:`/feature-documentation/nodes/PanoramaPrepareImages`
#. :doc:`/feature-documentation/nodes/LdrToHdrSampling`
#. :doc:`/feature-documentation/nodes/LdrToHdrCalibration`
#. :doc:`/feature-documentation/nodes/LdrToHdrMerge`
#. :doc:`/feature-documentation/nodes/FeatureExtraction`
#. :doc:`/feature-documentation/nodes/PanoramaInit`
#. :doc:`/feature-documentation/nodes/ImageMatching`
#. :doc:`/feature-documentation/nodes/FeatureMatching`
#. :doc:`/feature-documentation/nodes/PanoramaEstimation`
#. :doc:`/feature-documentation/nodes/SfMTransform`
#. :doc:`/feature-documentation/nodes/PanoramaWarping`
#. :doc:`/feature-documentation/nodes/PanoramaCompositing`
#. :doc:`/feature-documentation/nodes/ImageProcessing`
