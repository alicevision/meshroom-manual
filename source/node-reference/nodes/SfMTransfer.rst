SfMTransfer
===========

**Summary**

Retrieve poses and intrinsics from another reconstruction with matching views

settings

========================= ===========================================================================================================
Name                      Description
========================= ===========================================================================================================
Input                     SfMData file
Reference                 Path to the scene used as the reference to retrieve resolved poses and intrinsics.
Matching Method           Matching Method:
                          
                          * from_viewid: Align cameras with same view Id
                
                          * from_filepath: Align cameras with a filepath matching, using 'fileMatchingPattern'
                
                          * from_metadata: Align cameras with matching metadata, using 'metadataMatchingList'
                          
                          (**from_viewid**, from_filepath, from_metadata)
                          
File Matching Pattern     Matching regular expression for the "from_cameras_filepath" method.
                          You should capture specific parts of the filepath with parenthesis to define matching elements.
                          
                          Some examples of patterns:
                          
                          * Match the filename without extension (default value): **".*\/(.*?)\.\w{3}"**
                          
                          * Match the filename suffix after "_": ".*\/.*(_.*?\.\w{3})"
                          
                          * Match the filename prefix before "_": ".*\/(.*?)_.*\.\w{3}"
                          
Metadata                  
Metadata Matching List    List of metadata that should match to create the correspondences.
                          If the list is empty, the default value will
                          be used: ["Make", "Model", "Exif:BodySerialNumber", "Exif:LensSerialNumber"].
Poses                     Transfer poses. (**True**)
Intrinsics                Transfer cameras intrinsics. (**True**)
Verbose Level             verbosity level (fatal, error, warning, **info**, debug, trace).
Output                    SfMData file.
========================= ===========================================================================================================

