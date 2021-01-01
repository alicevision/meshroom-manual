Test Meshroom
=============

.. toctree::
   :maxdepth: 3
   
   reconstruction-eval/index.rst

For your first reconstruction in Meshroom, download the `Monstree Image
Dataset <https://github.com/alicevision/dataset_monstree>`__. You can
preview the Monstree model on
`Sketchfab <https://sketchfab.com/models/92468cb8a14a42f39c6ab93d24c55926>`__.

The Monstree dataset is known to work, so there should be no errors during the reconstruction.
This might be different when using your own image dataset.

Import the images in Meshroom by dragging and dropping them in the Images pane (left).
Alternatively, you can use the file dialog (File -> Import Images).
There are different folders in the Monstree dataset: full (all images), mini6
(6 images) and mini3 (3 images) to test out.

.. image:: /images/test_monstree_example.jpg

Press the 'Start' button (top) to run the reconstruction pipeline.
A progress bar will appear under the button.
When the progress bar gets to the end, the reconstruction is done.
This should take no more than 30 minutes on recent hardware.
Double-click the 'Texturing' node to load the final 3D output into the viewer.
Congratulations! You have successfully used Meshroom!