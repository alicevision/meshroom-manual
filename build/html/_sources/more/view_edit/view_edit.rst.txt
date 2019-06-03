View and Edit Models
=====================

Meshlab
-------


*You can drag and drop different OBJ and PLY files as layers.*

.. image:: 10000000000002800000016EE902B71EB0CF756B.jpg

*So in this case I have a layer for both the final mesh and the SFM points/cameras. Sometimes the mesh smoothing step can be a little too aggressive so I find it useful to compare between the original mesh and the smooth mesh. If the mesh looks broken, the PLY sfm data and the OBJ meshes are great for tracing through the pipeline.*


clean up / delete / smooth

The first thing you want to do is to rotate your model and align it with the coordinate system.

You can import the obj into
`Meshlab <http://www.meshlab.net/#download>`_
then go to
**Filters > Normals, Curvatures **
and
**Orientation > Transform: Rotate**
** **
and align it yourself from there.
** **

There might be some parts of the model or the scene you want to remove.

You can select ….. then remove...


`http://www.banterle.com/francesco/courses/2017/be_3drec/slides/Meshlab.pdf <http://www.banterle.com/francesco/courses/2017/be_3drec/slides/Meshlab.pdf>`_


`http:// <http://www.scanner.imagefact.de/tut/meshlabTut.pdf>`_

`www.scanner.imagefact.de/tut/meshlabTut.pdf <http://www.scanner.imagefact.de/tut/meshlabTut.pdf>`_

.. image:: 100000000000077C0000040C97D48F1AB92F97AD.png



Smooth mesh

If you don't like the smoothing results from Meshroom, you can smooth the mesh yourself.

`http://www.cs.cmu.edu/~reconstruction/advanced.html#meshlab <http://www.cs.cmu.edu/~reconstruction/advanced.html#meshlab>`_






Tutorials by
`Mister P. MeshLab Tutorials <https://www.youtube.com/channel/UC70CKZQPj_ZAJ0Osrm6TyTg>`_
`MeshLab Basics: Navigation <https://www.youtube.com/watch?v=Sl0vJfmj5LQ>`_

`MeshLab Basics: Selection, part one <https://www.youtube.com/watch?v=xj3MN7K6kpA>`_

`MeshLab Basics: Selection, part two <https://www.youtube.com/watch?v=Bc3GdJ6Ddsc>`_

`Cleaning: Triangles and Vertices Removal <https://www.youtube.com/watch?v=m2nmeJj5Ij4>`_

`Cleaning: Basic filters <https://www.youtube.com/watch?v=aoDLrXp1sfY>`_

`Mesh Processing: Decimation <https://www.youtube.com/watch?v=PWM6EGVVNQU>`_
`Meshlab Processing: Smoothing <https://www.youtube.com/watch?v=4mwm9eMJaXY>`_

`MeshLab Basics: Scale to real measures <https://www.youtube.com/watch?v=6psAppbOOXM>`_





Blender
-------


For detailed instructions visit the
`blender homepage <https://www.blender.org/>`_
or the
`blender  <https://www.youtube.com/user/BlenderFoundation>`_
`youtube channel <https://www.youtube.com/user/BlenderFoundation>`_
**.**

Here is a quick tutorial on how to optimize photogrammetry objects inside Blender: How to
3D
Photoscan Easy and Free!

`https://www.youtube.com/watch?v=k4NTf0hMjtY <https://www.youtube.com/watch?v=k4NTf0hMjtY>`_

meshing filtering 10:18 / 13:17 blender import


https://www.youtube.com/watch?v=RmMDFydHeso


Meshroom2Blender Blender Plugin
-------------------------------

`Blender <https://www.blender.org/>`_
importer of
`  <https://alicevision.github.io/#meshroom>`_
`AliceVision Meshroom <https://alicevision.github.io/#meshroom>`_
datafiles: cameras, images, sparse pointcloud and obj's.

Basic implementation of Meshroom importer. If you have s
o
phisticated node t
ree it will use only the first nodes from the file. Addon assumes you did compute each stages/nodes, and the output is same. Visit
`the Github project site <https://github.com/tibicen/meshroom2blender>`_
for details.

.. image:: 1000000000000637000002EDAEB94E9E7F951D6B.png

















BlenderLandscape
----------------


Addon for Blender 2.79b. 3DSurvey Collection of tools to improve the work-flow of a 3D survey (terrestrial or UAV photogrammetry). Import multiple objs at once (with correct orientation), for instance a bunch of models made in Meshroom.
`https://github.com/zalmoxes-laran/BlenderLandscape <https://github.com/zalmoxes-laran/BlenderLandscape>`_





Instant Meshes
--------------

`https://github.com/wjakob/instant-meshes <https://github.com/wjakob/instant-meshes>`_


includes quick intro


why do we want to use it?
It is a really fast auto-retopology solution and helps you create more accurate meshes


.. image:: 10000000000001040000010308083D38A3F5C0BA.png

CloudCompare
------------

open source
`https://www.danielgm.net/cc/ <https://www.danielgm.net/cc/>`_

`http://www.danielgm.net/cc/release/ <http://www.danielgm.net/cc/release/>`_


tut


http://www.danielgm.net/cc/tutorials.html


.. image:: 10000000000001C500000221611D09A26B69269B.png

Export model to Unity
---------------------

Start Unity, open your project and your asset folder.

Navigate in the file Explorer of your OS to the assets subfolder where you want to store your Photogrammetry object.


Copy the model.obj and texture.jpg (or other supported file types) from the Meshroom Export folder to the Unity assets subfolder.

Open Unity and wait for the auto-import to complete.


You might want to optimize your mesh
and texture for ingame use.

.. image:: 10000000000002DB000001F391C11C901F15F96E.png

Now you can add your model to the scene.


There is a little more to do to create a simple demo game, like adding a Mesh collider, optimize the texture,...


For detailed instructions visit the
`Unity homepage <https://unity3d.com>`_
.


Here is a manual on how to optimize photogrammetry objects inside Unity:
`Unity Photogrammetry Workflow <https://unity3d.com/files/solutions/photogrammetry/Unity-Photogrammetry-Workflow_2017-07_v2.pdf>`_
.. image:: 100000000000076E00000401AC14E84A53702851.png

Export to Maya (Plugin)
-----------------------

**MeshroomMaya**
(v0.4.2) is a Maya plugin that enables to model 3D objects from images.

Photomodeling plugin for Autodesk © Maya

MeshroomMaya allows graphic artists to do photomodeling on top of a 3D reconstruction (point cloud and cameras) with pixel precision.

.. image:: 100000000000043300000269241A429C4EFA5062.png

**Installation**

`https://github.com/alicevision/MeshroomMaya <https://github.com/alicevision/MeshroomMaya>`_


**Documentation**

`https://github.com/alicevision/MeshroomMaya/blob/develop/doc/Documentation.v0.4.2.md <https://github.com/alicevision/MeshroomMaya/blob/develop/doc/Documentation.v0.4.2.md>`_

**Start**

The first time you use MeshroomMaya, you need to load the plugin (via Window → Settings/Preferences → Plug-in Manager). Tick the autoload option to have it automatically loaded next time. You can now open the plugin window (via MeshroomMaya → Open).

**Load a project**

MeshroomMaya allows you to load a Meshroom reconstruction. Choose the Alembic file at the root of the project.

**Interface**

MeshroomMaya toolbar and parameters are presented as follow:

.. image:: 100002010000033A000001D4F2BAF14524E68A25.png

**Toolbar**

.. image:: 100002010000001900000017BE0E45595C15A4C9.png

Maya mode



.. image:: 100002010000001400000014D7CBF8DD27C71178.png

Creation mode (MVG)



.. image:: 100002010000001900000019CB2DE64F467FEE9C.png

Triangulation mode (MVG)



.. image:: 10000201000000190000001966F42B14327E46E8.png

Move base on point cloud mode (MVG)



.. image:: 10000201000000190000001935A738C2173FE04D.png

Move in adjacent plane mode (MVG)



.. image:: 100002010000001900000019BC8C7059248934AE.png

Locator mode (to reorient scene) (MVG)



.. image:: 100002010000001900000019788F9D71A52A186A.png

Open/Close parameters



.. image:: 100002010000001900000011CE0B1494B6DD45F1.png

Show cameras



.. image:: 1000020100000019000000198C66BF63556F817F.png

Show meshes



**Parameters**

.. image::100002010000001900000019E560F2A02F7AF416.png

Load .abc file



.. image:: 1000020100000019000000195B46B88089531FDC.png

Delete all 2D data.



.. image:: 10000201000000190000001133CAC1637D520F1C.png

Select closest camera from Maya perspective view.



.. image:: 100002010000001900000019BC8C7059248934AE.png

Set locator as origin of scene



*   **Thumbnail size**
Camera thumbnail size



*   **Display point cloud**
Show/hide pointcloud in plugin views.



*   **Active synchronisation**
Activate/Deactivate synchronisation on selection (meshes and cameras) between Maya and plugin



.. image:: 1000020100000019000000199CAE58C3513F1501.png

Remap images paths from alembic project file (if project as been moved for example)



*   **Camera Near & Far**
Set Near/Far Clip Planes for all cameras



*   **Camera Locator Scale**
Set camera locator size in viewport.



**Viewport**

.. image:: 100002010000025A000001B5BDE904C84A7ED6EB.png

One project is loaded, the different views are displayed below toolbar and parameters. You can choose which camera you want to display in MeshroomMaya viewports.

*   Mouse wheel : zoom and unzoom in image



*   Middle Mouse Button : move in image



**Modes**

*Creation*

.. image:: 100002010000001400000014D7CBF8DD27C71178.png

New face



Shortcut : CTRL + 0

This tool enables to create a face according to point cloud. You have to create four points.

**Note**
: If no plane is detected when you are putting the last point of the face, the polygon will be displayed in red.

.. image:: 100002010000001400000014D7CBF8DD27C71178.png

Extend a face



A new face can be create from an existing edge. You have to click the edge and move it.

**Tip**
: Pressing
**V**
key, the new created face will snap to existing edges and points..


*Move*

.. image:: 100002010000001900000019CB2DE64F467FEE9C.png

Triangulation



Shortcut : CTRL + 1

This tool enable to set a 3D point more precisely from 2D points clicked on MeshroomMaya view. It does not use the point cloud at all. You need to set this point in at least two views.

Pressing "Enter"’ key, the 2D positions will be erased.

**Note**
: The more views the point is placed in, the more accurate the 3D position will be. The number of views in which the points have been placed is displayed for all points.


**Warning**
: Mesh should not have transform value. You have to make a freeze transform if you created it with Maya.

.. image:: 10000201000000190000001966F42B14327E46E8.png

Move base on point cloud



Shortcut : CTRL + 2

Point or edge is moved in a new plane, computed from point cloud.

.. image:: 10000201000000190000001935A738C2173FE04D.png

Move in adjacent plane



Shortcut : CTRL + 3

Point or edge is moved in the plane in which it already is.


*Locator*

.. image:: 100002010000001900000019BC8C7059248934AE.png

Create locator by triangulation



This tool enables to set a locator by triangulated its position. You need to place a 2D point on at least two different views. The 3D position will be automatically computed and locator will be created there.

**Tip**
: The more 2D points there is, the more the 3D position will be accurate.

Once the locator created, it can be adjusted with Maya tools (rotation, scale, move, …) Once correctly place, you have to click on the Locator button in parameters

.. image:: 100002010000001900000019BC8C7059248934AE.png

to apply the transformation.

*   Create locator from vertex



Locator can also be created from an existing vertex. You have to set vertex selection mode and select the vertex from which you want to create the locator. Then, in MeshroomMaya menu, click on "Create locator from vertex".

.. image:: 10000201000000AA00000038335512F26BC1BA43.png

Proceed as in "Create locator by triangulation" section to place it more precisely and click on Locator button in parameters (

.. image:: 100002010000001900000019BC8C7059248934AE.png

) to apply transformation.

**Cameras**

To set a camera in one of the MeshroomMaya view, click on the corresponding thumbnail.

**Tip**
: If you select a camera in Maya, it automatically selects it in MeshroomMaya and load it in the left viewport. You can also select the camera directly from MeshroomMaya.

.. image:: 10000201000001EB00000184E4DA06C84C30A119.png

**Meshes**

To display meshes list, click on icon
.. image:: mesh.png

.. image:: 1000020100000019000000198C66BF63556F817F.png
.

Meshes can be activated/deactivated in plugin.

**Tip**
: In order to optimize performance, it’s recommended to deactivate meshes that are not used for modeling.

Alembic bridge
~~~~~~~~~~~~~~

*Export from MeshroomMaya*

Select meshes and cameras to export. Click on menu : "MeshroomMaya > Export selection as ABC" to choose file location.

*Import in Nuke/Mari*

In menu "NukeMVG > Import Alembic" , .abc file can be loaded. The tool create the graph of camera projection. Result can be export to Mari via Nuke<>Mari bridge.

.. image:: 1000000000000500000002D057790BC5AE108E3F.png

SideFX Houdini Plugin
---------------------

An implementation of *Alicevision* is available in Houdini as part of the (free) GameDevelopmentToolset.


You can find Installation Instructions on the following page:
`https://www.sidefx.com/tutorials/alicevision-plugin/ <https://www.sidefx.com/tutorials/alicevision-plugin/>`_


Review (german):

`https://www.digitalproduction.com/2019/02/26/alicevision-photogrammetrie-in-houdini/ <https://www.digitalproduction.com/2019/02/26/alicevision-photogrammetrie-in-houdini/>`_


Students can download the free learning edition called
`  <https://www.sidefx.com/products/compare/>`_
`Houdini Apprentice <https://www.sidefx.com/products/compare/>`_
. This is a node-locked license that has all the features of Houdini FX with some restrictions such as a limited render size and a watermark on final renderings.
