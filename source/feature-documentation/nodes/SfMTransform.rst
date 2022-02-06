SfMTransform
============

Description
-----------

Transform/Scale SfM using given transformation, cameras, landmarks, markers.
Can be used to scale SfM to real-world size.

Settings
--------

========================= ===========================================================================================================
Name                      Description
========================= ===========================================================================================================
Input                     SfMData file
Transformation Method     Transformation method:

                          * transformation: Apply a given transformation
                      
                          * auto_from_cameras: Use cameras
                      
                          * **auto_from_landmarks**: Fit all landmarks into a box [-1,1]

                          * from_single_camera: Use a specific camera as the origin of the coordinate system
                      
                          * from_markers: Align specific markers to custom coordinates
                          
                          * from_gps: Align using the gps metadata (EXIF)
                          
Transformation            Required only for 'transformation' and 'from_single_camera' methods:
                      
                          * transformation: Align [X,Y,Z] to +Y-axis, rotate around Y by R deg, scale by S; syntax: X,Y,Z;R;S
                      
                          * from_single_camera: Camera UID or image filename
Landmarks Describer Types Image describer types used to compute the mean of the point cloud. (only for "landmarks" method).
                          (**'sift'**, 'sift_float', 'sift_upright', **'akaze'**, 'akaze_liop', 'akaze_mldb', 'cctag3', 'cctag4',
                          'sift_ocv', 'akaze_ocv')
Additional Scale          Additional scale to apply. (0.0-100.0, default **1.0**)  
Markers                   Markers alignment points
Scale                     Apply scale transformation.
Rotation                  Apply rotation transformation.
Translation               Apply translation transformation.
Verbose Level             verbosity level (fatal, error, warning, **info**, debug, trace).
========================= ===========================================================================================================


Details
--------

Transformation Method: transformation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``transformation`` as ``X,Y,Z;R;S``
    Align ``[X,Y,Z]`` to +Y-axis, rotate around ``Y`` by ``R`` deg, scale by ``S``.
    It aligns and scales the point cloud by explicitly specifying the scale and
    "up" vector [X,Y,Z] in the point cloud's reference system.
    The rotation is computed such that the specified [X,Y,Z] vector is aligned with [0,1,0] after
    the transformation.

    The use-case to allow the user to derive the desired rotation by
    interactive manipulation of the point cloud in a 3D program (Meshlab),
    read off the transformation parameters and transform the point cloud.
    https://github.com/alicevision/AliceVision/pull/206

* ``from single camera`` as ``UID`` or ``image filename``
    Sets a specific camera as origin and applies correct orientation if possible
    Provide Camera **UID** or **image filename**

* ``auto_from_landmarks`` as DescriberType(s)
    Compute the scale that brings all the selected landmarks type in a the unit box [-1, 1]
