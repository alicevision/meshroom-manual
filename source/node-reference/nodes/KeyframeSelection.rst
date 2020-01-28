KeyframeSelection
=================

**Description** 

This is a node for keyframe selection from video, which removes too similar or too blurry images.

Note: At the moment, KeyframeSelection can not be used as input for CameraInit.
To automatically add extracted frames to your project you can copy the output folder path of KeyframeExtraction and set it as the Live Reconsturuction Image Folder Path. Then start watching the folder and execute the graph.
``https://github.com/alicevision/meshroom/issues/232``

MR version 2020.x

settings

============================= =================================================================================================
Name                          Description
============================= =================================================================================================
Media Path                    Media Path
Media Paths                   Input video files or image sequence directories.
Brand                         Camera brand.
Brands                        Camera brands.
Model                         Camera model.
Models                        Camera models.
mmFocal                       Focal in mm (will be use if not 0). (**0.0**-500)
mmFocals                      Focals in mm (will be use if not 0).
pxFocal                       Focal in px (will be use and convert in mm if not 0). (**0.0**-500)
pxFocals                      Focals in px (will be use and convert in mm if not 0).
Frame Offset                  Frame Offset **0**-100
Frame Offsets                 Frame Offsets
Sensor Db Path                Camera sensor width database path. (ALICEVISION_SENSOR_DB)
Voctree Path                  Vocabulary tree path. (ALICEVISION_VOCTREE)
Use Sparse Distance Selection Use sparseDistance selection in order to avoid similar keyframes. (**True**)
Use Sharpness Selection       Use frame sharpness score for keyframe selection. (**True**)
Sparse Distance Max Score     Maximum number of strong common points between two keyframes. (1-200, **100**)
Sharpness Preset              Preset for sharpnessSelection : {ultra, high, **normal**, low, very_low, none}
Sharp Subset                  sharp part of the image (1 = all, 2 = size/2, ...) (1-100, **4**)
Min Frame Step                minimum number of frames between two keyframes (1-100, **12**)
Max Frame Step                maximum number of frames after which a keyframe can be taken (2-1000,  **36**)
Max Nb Out Frame              maximum number of output frames (0 = no limit) (**0**-10000)
Verbose Level                 ['fatal', 'error', 'warning', 'info', 'debug', 'trace']
Output Folder                 Output keyframes folder for extracted frames. (internalFolder)
============================= =================================================================================================
