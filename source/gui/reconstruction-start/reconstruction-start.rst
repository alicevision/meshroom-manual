Start Reconstruction
=====================

Click the green **Start** button to start processing. 
To stop/pause click the **Stop** button. The progress will be kept.

There are two progress bars: the line below the **menu bar** indicating the overall progress
and the other in the **Graph Editor** within the **nodes**.
To get a detailed progress log, open the **CommandLine** window
or click on the **node** you are interested in and go to the Log tab in the properties pane of the **Graph Editor**.


You can open the (Your-Project-Folder) ``->`` **MeshroomCache** to see the output of each node. (Shortcut: Icon and path at the bottom left side of the main window)

A node folder contains the output of the node.
By default Meshroom uses a unique id to name the output folders to prevent overwriting data and already computed results of the project can be reused.

**Example**: You are not satisfied with your first result and make changes to the **StructureFromMotion** node. The new output will be placed under a different name inside the  **StructureFromMotion** Folder.

You can change the **name of the output folders** of your nodes by clicking on the node and changing the **Output Folder** name in the **Attributes tab** of the **Graph Editor** Properties pane.