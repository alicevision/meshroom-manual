DepthMapFilter
==============

**Description**

The original depth maps will not be entirely consistent. Certain depth
maps will claim to see areas that are occluded by other depth maps. The
DepthMapFilter step isolates these areas and forces depth consistency.

settings

======================================= =================================================================================
Name                                    Description
======================================= =================================================================================
Input                                   SfMData file
Depth Map Folder                        Input depth map folder
Number of Nearest Cameras               Number of nearest cameras used for filtering 10 (0 - 20)
Min Consistent Cameras                  Min Number of Consistent Cameras 3 (0 - 10)
Min Consistent Cameras Bad Similarity   Min Number of Consistent Cameras for pixels with weak similarity value 4 (0 - 10)
Filtering Size in Pixels                Filtering size in Pixels (0 - 10)
Filtering Size in Pixels Bad Similarity Filtering size in pixels (0 - 10)
Verbose Level                           verbosity level (fatal, error, warning, info, debug, trace)
Output                                  Output folder for generated depth maps
======================================= =================================================================================

**Min Consistent Cameras** lower this value if the Meshing node has 0
depth samples input

**View Output** open output folder and view EXR files
