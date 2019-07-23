Related Projects
================


..image:: ofxMVG.jpg

ofxMVG
------

Camera Localization OpenFX Plugin for Nuke

`https://github.com/alicevision/ofxMVG <https://github.com/alicevision/ofxMVG>`_

Not available at the moment.



..image:: marker2.jpg

CCTag
-----

Concentric Circles Tag

This library allows you to detect and identify CCTag markers. Such marker system can deliver sub-pixel precision while being largely robust to challenging shooting conditions.
`https://github.com/alicevision/CCTag <https://github.com/alicevision/CCTag>`_

**CCTag library**

Detection of CCTag markers made up of concentric circles. Implementations in both CPU and GPU.

**See paper**
: "Detection and Accurate Localization of Circular Fiducials under Highly Challenging Conditions." Lilian Calvet, Pierre Gurdjos, Carsten Griwodz and Simone Gasparini. CVPR 2016.

`https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Calvet_Detection_and_Accurate_CVPR_2016_paper.pdf <https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Calvet_Detection_and_Accurate_CVPR_2016_paper.pdf>`_

**Marker library**

Markers to print are located `here <https://github.com/alicevision/CCTag/blob/develop/markersToPrint>`_
.

**WARNING**
Please respect the provided margins. The reported detection rate and localization accuracy are valid with completely planar support: be careful not to use bent support (e.g. corrugated sheet of paper).

The four rings CCTags will be available soon.

CCTags requires either CUDA 8.0 and newer or CUDA 7.0 (CUDA 7.5 builds are known to have runtime errors on some devices including the GTX980Ti). The device must have at least compute capability 3.5.

Check your graphic card CUDA `compatibility
here <https://github.com/tpruvot/ccminer/wiki/Compatibility>`_
.

..image:: marker3.jpg

PopSIFT
-------

Scale-Invariant Feature Transform (SIFT)

This library provides a GPU implementation of SIFT. 25 fps on HD images on recent graphic cards.
`https://github.com/alicevision/popsift <https://github.com/alicevision/popsift>`_
