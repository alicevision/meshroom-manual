Live Reconstruction
===================

Live reconstruction is meant to be used along with a camera that can transfer images to a computer while shooting (using wifi, a wifi sd-card or Tethering). 
Meshroom can watch a folder for new images and successively augment previous SfM (point clouds + cameras) after each {Min. Images} per Step. This allows to get an iterative preview during shooting, e.g to see which areas of the dataset requires more coverage.

To enable **Live Reconstruction** go to the menu bar **View :math:`\Rightarrow` Live Reconstruction**
A new **Live Reconstruction** pane will appear under the Images pane.

For each new import, a new **Image Group** inside the **Images** pane will be created.
Also the **Graph Editor** updates the graph, adding nodes to process the newly added images and add them to the pipeline.

Select the **Image Folder** to watch and the minimum of new images folder to be imported per step.
Click **Start** in the **Live Reconstruction** pane to start monitoring the selected folder for new files. 
You should then see in the graph one branch (from **CameraInit** to **StructureFromMotion**) for each batch of images. 1
The reconstruction process will stop at the last processed **StructureFromMotion** node and will not automatically go through the rest of the default pipeline.
This is for practical reasons. The point cloud will update in real time with newly added images. Computing the mesh for every new image batch is not effective.

Once you complete the image capturing process, click **Stop** and disconnect the **PrepareDenseScene** node from the first **StructureFromMotion** node and connect it with the last **StructureFromMotion** node.

.. image:: /images/gui/image-gallery/live_graph.jpg

.. image:: /images/gui/image-gallery/live_reconstruction.jpg

.. image:: /images/gui/image-gallery/live_reconnect_graph.jpg

.. note:: The groups will be merged using the **ImageMatchingMultiSfM** node. Read the node description for details.

A demo video can be found here: https://www.youtube.com/watch?v=DazLfZXU_Sk