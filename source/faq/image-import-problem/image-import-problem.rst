Images cannot be imported
=========================

The import module from AliceVision has problems parsing corrupted image
files. Some mobile phone cameras and action cams/small cameras like the
CGO3+ from Yuneec produce images which are not valid. Most image viewers
and editing software can handle minor inconsistencies.

Use tools like `Bad Peggy`_ to `check for errors`_ in your image files.

e.g. "*...extraneous bytes before marker 0xdb*".

or "Truncated File - Missing EOI marker" on a raspberry camera

To fix this problem, you need to bulk convert your dataset (this is why
downscaling worked too). You can use IrfranView
``File->Batch Conversion`` or Imagemagick. Make sure you set the quality
to 100%. Now you can add the images to Meshroom (assuming the camera is
in the sensor db).

--

**drag and drop of images does not work** (`#149`_) mouse over the with
any photos the cursor is disabled and dropping photos into the viewport
has no effect. Do you run Meshroom as admin? If yes, that's the cause.
Windows disables drag and drop on applications being run as admin.

--

Note: avoid special characters/non-ASCII characters in Meshroom and
images file paths (`#209`_)

.. _Bad Peggy: https://www.coderslagoon.com/
.. _check for errors: http://openpreservation.org/blog/2016/11/29/jpegvalidation/
.. _#149: https://github.com/alicevision/meshroom/issues/149
.. _#209: https://github.com/alicevision/meshroom/issues/209