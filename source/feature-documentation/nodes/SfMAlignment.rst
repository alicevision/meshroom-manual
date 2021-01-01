SfMAlignment
============

**Description**

Align SfM file to a scene

settings

======================= =================================================================================================
Name                    Description
======================= =================================================================================================
Input                   SfMData file
Reference               Path to the scene used as the reference coordinate system
Alignment Method        Alignment Method:

                        * **from_cameras_viewid**: Align cameras with same view Id

                        * from_cameras_poseid: Align cameras with same pose Id

                        * from_cameras_filepath: Align cameras with a filepath matching, using 'fileMatchingPattern'

                        * from_cameras_metadata: Align cameras with matching metadata, using 'metadataMatchingList'

                        * from_markers: Align from markers with the same Id
File Matching Pattern   Matching regular expression for the "from_cameras_filepath" method.
                        You should capture specific parts of the filepath with parenthesis to define matching elements.
                        
                        Some examples of patterns:
                        
                        * Match the filename without extension (default value): **".*\/(.*?)\.\w{3}"**
                        
                        * Match the filename suffix after "_": ".*\/.*(_.*?\.\w{3})"
                        
                        * Match the filename prefix before "_": ".*\/(.*?)_.*\.\w{3}"
Metadata                
Metadata Matching List  List of metadata that should match to create the correspondences. 
                        If the list is empty, the default value will be used:
                        ["Make", "Model", "Exif:BodySerialNumber", "Exif:LensSerialNumber"].
Scale                   Apply scale transformation. (**True**)
Rotation                Apply rotation transformation. (**True**)
Translation             Apply translation transformation. (**True**)
Verbose Level           ['fatal', 'error', 'warning', 'info', 'debug', 'trace']
Output                  Aligned SfMData file internalFolder + 'alignedSfM.abc
======================= =================================================================================================
