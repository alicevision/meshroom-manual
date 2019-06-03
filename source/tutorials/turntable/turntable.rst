Turntable
=============

As mentioned in chapter X, it is possible to use a turntable.




Have you ever heard about masking? Currently, meshroom does not support masking but you can see #188 for a decent workaround.

Essentially, the software is detecting features on both the foreground and background. On a turntable, the subject is moving but the background is not. This confuses it.

So you have 2 choices: make the background completely white and same lighting so that no features can be extracted from this region, or mask your images - that is basically covering the background artificially to stop the region being used in the pipeline, or both.


*Another approach entirely would be to just keep the scene the same but you move the camera instead, which is usually the best way to go about things anyway, this what I would most recommend.*


*   without masking, the object on the turntable will become blurry/only partially reconstructed and the background will be reconstructed fine



*   we use a blank background to easily mask it




simply using your white wallpaper will not work as it has too many recognizable features you should use a clean and smooth background that will not allow any feature detection use the "Scale for Small-Object Photogrammetry" by Samantha Porter
`  <http://www.stporter.com/resources/>`_
`http://www.stporter.com/resources/ <http://www.stporter.com/resources/>`_
`  <https://conservancy.umn.edu/handle/11299/172480?show=full>`_
`https://conservancy.umn.edu/handle/11299/172480?show=full <https://conservancy.umn.edu/handle/11299/172480?show=full>`_

or create your own
