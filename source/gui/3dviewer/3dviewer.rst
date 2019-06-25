3D Viewer
=========

.. image:: 3dviewer.png

The **3D Viewer** will preview the SfM Pointcloud, cameras and the Mesh preview.
You can use your mouse or the rotate/scale toolbar on the left. You can hold **Shift** to pan. Press **F** to reset the view. **Double-click** to create a new rotation center for the Mesh.
To display the final model, a button will appear on the bottom side to load the mesh (**Load model**). Uncheck the SfM layer for a better view.
To refit the 3D-model to the new dimensions of the pane if you changed its size, right-click to display a menu with refitting options.

.. image:: settings.png

By default **StructureFromMotion** and **Texturing** results will be added to your **Scene** layers. You can add the outputs of other node variations to your Scene in the **3D Viewer** by double clicking on the nodes. Supported nodes: StructureFromMotion, Texturing, MeshDecimate, MeshDenoise, MeshResampling

**3D Model**
The final 3D-Model will be saved in **Project Folder →MeshroomCache → Texturing**

By default it will be saved in the OBJ format. You can change it in the node settings.

.. Note:: 
  
  At the moment Meshroom does not support model realignment, so the model can be orientated upside down relative to the grid. You can change the orientation in another software like Meshlab.