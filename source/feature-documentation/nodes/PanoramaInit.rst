PanoramaInit
============

**Description**

This node allows to setup the Panorama:
1/ Enables the initialization the cameras from known position in an XML file (provided by a motorized panorama head).
2/ Enables to setup Full Fisheye Optics (to use an Equirectangular camera model).
3/ To automatically detects the Fisheye Circle (radius + center) in input images or manually adjust it.

settings

============================== =================================================================================================
Name                           Description
============================== =================================================================================================
Input                          SfM Data File
Xml Config                     XML Data File (Papywizard xml file format)
Dependency                     Folder(s) in which computed features are stored. (WORKAROUND for valid Tractor graph submission)
Full Fisheye                   To declare a full fisheye panorama setup
Estimate Fisheye Circle        Automatically estimate the Fisheye Circle center and radius instead of using user values.
Fisheye Center                 Center of the Fisheye circle (XY offset to the center in pixels).
Radius                         Fisheye visibillity circle radius (% of image shortest side).
input Angle offset             Add a rotation to the input XML given poses (CCW).
Debug Fisheye Circle Detection Debug fisheye circle detection.
Verbose Level                  ['fatal', 'error', 'warning', 'info', 'debug', 'trace']
Output                         Output sfmData.
============================== =================================================================================================

