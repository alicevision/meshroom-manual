ImageMatching
=============

**Description**

This is a preprocessing step which figures out which images make sense to match to each other.


settings

======================== ============================================================================================================================================
Name                     Description
======================== ============================================================================================================================================
Image                    SfMData file
Features Folders         Folder(s) containing the extracted features and descriptors
Tree                     Input name for the vocabulary tree file ALICEVISION_VOCTREE
Weights                  Input name for the weight file, if not provided the weights will be computed on the database built with the provided set
Minimal Number of Images Minimal number of images to use the vocabulary tree. If we have less features than this threshold, we will compute all matching combinations
Max Descriptors          Limit the number of descriptors you load per image. Zero means no limit
Nb Matches               The number of matches to retrieve for each image (If 0 it will retrieve all the matches) 50 (0-1000)
Verbose Level            verbosity level (fatal, error, warning, info, debug, trace)
Output List File         Filepath to the output file with the list of selected image pairs
======================== ============================================================================================================================================

**Detailed descriptioin**

The objective of this part is to find images that are looking to the same areas of the scene. For that, we use the image retrieval techniques to find images that share some content without the cost of resolving all feature matches in details. The ambition is to simplify the image in a compact image descriptor which allows to compute the distance between all images descriptors efficiently.

One of the most common method to generate this image descriptor is the vocabulary tree approach. By passing all extracted features descriptors into it, it makes a classification by comparing their descriptors to the ones on each node of this tree. Each feature descriptor ends up in one leaf, which can be stored by a simple index: the index of this leaf in the tree. The image descriptor is then represented by this collection of used leaves indices.

It is now possible to see if different images share the same content by comparing these image descriptors.

[Nister2006] 	Scalable Recognition with a Vocabulary Tree, David Nister and Henrik Stewenius, CVPR 2006
