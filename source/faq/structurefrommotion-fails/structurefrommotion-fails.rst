StructureFromMotion fails
=========================

``StructureFromMotion`` may fail when there is not enough features
extracted from the image dataset (weakly textured dataset like indoor
environment). In this case, you can try to augment the amount of
features:

-  ``DescriberPreset`` to ``High`` or ``Ultra`` in ``FeatureExtraction``
-  Add ``AKAZE`` as ``DescriberType`` on ``FeatureExtraction``,
   ``FeatureMatching`` and ``StructureFromMotion`` nodes

Using more features will reduce performances on large datasets. Another
problem is that adding too much features (less reliable) may also reduce
the amount of matches by creating more ambiguities and conflicts during
features matching.

-  ``Guided Matching`` parameter on ``FeatureMatching`` is useful to
   reduce conflicts during feature matching but is costly in
   performance. So it is very useful when you have few images (like a
   cameras rig from a scan studio).