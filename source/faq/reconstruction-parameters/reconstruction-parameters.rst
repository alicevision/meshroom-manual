Reconstruction parameters
=========================

The default parameters are optimal for most datasets. Also, many
parameters are exposed for research & development purposes and are not
useful for users. A subset of them can be useful for advanced users to
improve the quality on specific datasets.

The first thing is to verify the number of reconstructed cameras from
your input images. If a significant number are not reconstructed, you
should focus on the options of the sparse reconstruction.

Sparse reconstruction
---------------------

1. ``FeatureExtraction``: Change ``DescriberPreset`` from ``Normal`` to
   ``High`` If your dataset is not big (<300 images), you can use
   ``High`` preset. It will take more time for the
   ``StuctureFromMotion`` node but it may help to recover more cameras.
   If you have really few images (like <50 images), you can also try
   ``Ultra`` which may improve or decrease the quality depending on the
   image content.

2. ``FeatureMatching``: Enable ``Guided Matching`` This option enables a
   second stage in the matching procedure. After matching descriptor
   (with a global distance ratio test) and first geometric filtering, we
   retrieve a geometric transformation. The guided-matching use this
   geometric information to perform the descriptors matching a second
   time but with a new constraint to limit the search. This
   geometry-aware approach prevents early rejection and improves the
   number of matches in particular with repetitive structures. If you
   really struggle to find matches it could be beneficial to use
   ``BRUTE_FORE_L2`` matching, but this is not good in most cases as it
   is very inefficient.

3. Enable ``AKAZE`` as ``DescriberTypes`` on ``FeatureExtraction``,
   ``FeatureMatching`` and ``StructureFromMotion`` nodes It may improve
   especially on some surfaces (like skin for instance). It is also more
   affine invariant than SIFT and can help to recover connections when
   you have not enough images in the input.

4. To improve the robustness of the initial image pair selection/initial
   reconstruction, you can use a SfM with ``minInputTrackLength`` set to
   3 or 4 to keep only the most robust matches (and improve the ratio
   inliers/outliers). Then, you can chain another SfM with the standard
   parameters, so the second one will try again to localize the cameras
   not found by the first one but with different parameters. This is
   useful if you have only a few cameras reconstructed within a large
   dataset.
   
Dense reconstruction
--------------------

1. | ``DepthMap``
   | You can adjust the ``Downscale`` parameter to drive
     precision/computation time. If the resolution of your images is not
     too high, you can set it to 1 to increase precision, but be
     careful, the calculation will be ~4x longer. On the contrary,
     setting it to a higher value will decrease precision but boost
     computation.
   | Reduce the number of neighbour cameras
     (``SGM: Nb Neighbour Cameras``, ``Refine: Nb Neighbour Cameras``)
     will directly reduce the computation time linearly, so if you
     change from 10 to 5 you will get a 2x speedup. A minimum value of 3
     is necessary, 4 already gives decent results in many cases if the
     density of your acquisition process regular enough. The default
     value is necessary in a large scale environment where it is
     difficult to have 4 images that cover the same area.

2. | ``DepthMapFilter``
   | If you input images are not dense enough or too blurry and you have
     too many holes in your output. It may be useful to relax the
     ``Min Consistent Cameras`` and
     ``Min Consistent Cameras Bad Similarity`` to 2 and 3 respectively.

3. | ``Meshing``
   | If you have less than 16G of RAM, you will need to reduce the
     ``Max Points`` to fit your RAM limits. You may also augment it, to
     recover a more dense/precise mesh.

4. | ``MeshFiltering``
   | ``Filter Large Triangles Factor`` can be adjusted to avoid holes or
     on the other side to limit the number of large triangles.
     ``Keep Only The Largest Mesh``: Disable this option if you want to
     retrieve unconnected fragments that may be useful.

5. | ``Texturing``
   | You can change the ``Texture Downscale`` to 1 to improve the
     texture resolution.

Describer Types
---------------

You can choose to use one or multiple describer types. If you use
multiple types, they will be combined together to help get results in
challenging conditions. *The values should always be the same between
FeatureExtraction, FeatureMatching and StructureFromMotion.* The only
case, you will end up with different values is for testing and comparing
results: in that case you will enable all options you want to test on
the FeatureExtraction and then use a subset of them in Matching and SfM.