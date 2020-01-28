SketchfabUpload
===============

**Description**

Sketchfab is a popular website to share and view 3D files,
this provides a node to allow direct upload to Sketchfab from Meshroom.
API key is provided by the user in the node settings.

MR version: 2020.x

settings

============= ===========================================================
Name          Description
============= ===========================================================
Input Files   Input Files to export
API Token     Get your token from https://sketchfab.com/settings/password
Title         Title cannot be longer than 48 characters.
Description   Description cannot be longer than 1024 characters.
License       'CC Attribution', 'CC Attribution-ShareAlike',
              'CC Attribution-NoDerivs', 'CC Attribution-NonCommercial',
              'CC Attribution-NonCommercial-ShareAlike',
              'CC Attribution-NonCommercial-NoDerivs'
Tag           Tag cannot be longer than 48 characters.
Tags          Maximum of 42 separate tags.
Category      Adding categories helps improve the discoverability of your
              model. ('none', 'animals-pets', 'architecture',
              'art-abstract', 'cars-vehicles', 'characters-creatures',
              'cultural-heritage-history', 'electronics-gadgets',
              'fashion-style', 'food-drink', 'furniture-home',
              'music', 'nature-plants', 'news-politics', 'people',
              'places-travel', 'science-technology', 'sports-fitness',
              'weapons-military')
Publish       If the model is not published it will be saved as a draft.
              (False)
Inspectable   Allow 2D view in model inspector. (True)
Private       Requires a pro account. (False)
Password      Requires a pro account.
Verbose Level verbosity level (critical, error, warning, info, debug).
============= ===========================================================

**usage:**

|image0|

.. |image0| image:: SketchfabUpload.JPG
   :target: SketchfabUpload.JPG
